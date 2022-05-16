from fastapi import APIRouter
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario
from src.infra.sqlalchemy.repository.usuario import RepositoryUsuario
from src.infra.sqlalchemy.config.database import get_db
from typing import List

router = APIRouter()

#------ ROTAS PARA USUARIOS ------#
@router.get('/usuarios', response_model=List[Usuario])
def listar_usuarios(session_db: Session = Depends(get_db)):
    usuarios = RepositoryUsuario(session_db).listar()
    return usuarios

@router.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session_db: Session = Depends(get_db)):
    usuario_criado = RepositoryUsuario(session_db).criar(usuario)
    return usuario_criado