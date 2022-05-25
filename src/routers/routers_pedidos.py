from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models.models import Usuario
from src.routers.auth_utils import obter_usuario_logado
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Pedido, Usuario
from src.infra.sqlalchemy.repository.pedido import RepositoryPedido

router = APIRouter()

@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedido(pedido: Pedido, session_db: Session = Depends(get_db)):
    pedido = RepositoryPedido(session_db).criar(pedido)
    return pedido

@router.get('/pedidos/users', response_model=List[Pedido])
def listar_pedidos(session_db: Session = Depends(get_db)):
    pedidos = RepositoryPedido(session_db).listar()
    return pedidos

@router.get('/pedidos/{pedido_id}', response_model=Pedido)
def exibir_pedido(pedido_id: int, session_db: Session = Depends(get_db)):
    try:
        pedido = RepositoryPedido(session_db).buscar_pedido_by_id(pedido_id)
        return pedido
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um pedido com ID = {pedido_id}')

@router.get('/pedidos', response_model=List[Pedido])
def exibir_pedido(usuario: Usuario = Depends(obter_usuario_logado), session_db: Session = Depends(get_db)):
    pedido = RepositoryPedido(session_db).buscar_pedidos_by_usuario_id(usuario.id)

    if not pedido:   
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existem compras para o Usuario de ID = {usuario.id}')

    return pedido
    
@router.get('/pedidos/{usuario_id}/vendas')
def exibir_pedido(usuario_id: int, session_db: Session = Depends(get_db)):
    pedido = RepositoryPedido(session_db).buscar_vendas_by_usuario_id(usuario_id)
    
    if not pedido:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existem vendas para o Usuario de ID = {usuario_id}')
    return pedido