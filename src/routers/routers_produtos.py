from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repository.produto import RepositoryProduto
from typing import List

router = APIRouter()

#------ ROTAS PARA PRODUTOS ------#
@router.get('/produtos', response_model=List[Produto])
def listar_produtos(session_db: Session = Depends(get_db)):
    produtos = RepositoryProduto(session_db).listar()
    return produtos

@router.post('/produtos')
def criar_produto(produto: Produto, session_db: Session = Depends(get_db)):
    produto = RepositoryProduto(session_db).criar(produto)
    return produto

@router.get('/produtos/{produto_id}')
def exibir_produto(produto_id: int, session_db: Session = Depends(get_db)):
    produto = RepositoryProduto(session_db).buscarPorId(produto_id)
    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um produto com ID = {produto_id}')
    
    return produto

@router.put('/produtos/{produto_id}')
def editar_produto(produto_id:int, produto: Produto, session_db: Session = Depends(get_db)):
    RepositoryProduto(session_db).editar(produto_id, produto)
    return {"message" : "produto atualizado com sucesso!"}

@router.delete('/produtos/{produto_id}')
def editar_produto(produto_id: int, session_db: Session = Depends(get_db)):
    RepositoryProduto(session_db).remover(produto_id)
    return {"message" : "produto removido com sucesso!"}
