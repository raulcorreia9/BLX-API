from fastapi import APIRouter, HTTPException
from fastapi import Depends, status
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario, UsuarioSimples, LoginData, LoginSucesso
from src.infra.sqlalchemy.repository.usuario import RepositoryUsuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import hash_provider
from src.infra.providers import token_provider
from src.routers.auth_utils import obter_usuario_logado
from typing import List

router = APIRouter()

#------ ROTAS PARA USUARIOS ------#
@router.get('/usuarios', response_model=List[UsuarioSimples])
def listar_usuarios(session_db: Session = Depends(get_db)):
    usuarios = RepositoryUsuario(session_db).listar()
    return usuarios

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session_db: Session = Depends(get_db)):
    
    #Verifica se ja existe usuario cadastrado com o telefone passado
    usuario_localizado = RepositoryUsuario(session_db).find_by_telefone(usuario.telefone)
    
    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail=f'Telefone ja cadastrado!')
    else:        
        usuario.senha = hash_provider.gerar_hash(usuario.senha)
        usuario_criado = RepositoryUsuario(session_db).criar(usuario)
        
        return usuario_criado

@router.get('/usuarios/{usuario_id}', response_model=UsuarioSimples)
def exibir_usuario(usuario_id: int, session_db: Session = Depends(get_db)):
    usuario = RepositoryUsuario(session_db).find_by_id(usuario_id)
    
    if not(usuario):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existem compras para o Usuario de ID = {usuario_id}')
    return usuario

@router.post('/auth/token')
def login(login_data: LoginData, session_db: Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone
    
    usuario = RepositoryUsuario(session_db).find_by_telefone(telefone)
    
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone invalido')

    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)
    
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Senha invalida')

    #Gera JWT
    token = token_provider.criar_acess_token({'sub': usuario.telefone})
    
    return LoginSucesso(usuario=usuario, access_token=token)

@router.get('/auth/me', response_model=UsuarioSimples)
def me(usuario: Usuario = Depends(obter_usuario_logado)):
    return usuario