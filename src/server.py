from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples
from src.schemas.schemas import Usuario
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repository.produto import RepositoryProduto
from src.infra.sqlalchemy.repository.usuario import RepositoryUsuario

#uvicorn src.server:app --reload --reload-dir=src
#fastapi\Scripts\activate

criar_bd()

app = FastAPI()

#------ ROTAS PARA PRODUTOS ------#
@app.get('/produtos', response_model=List[Produto])
def listar_produtos(session_db: Session = Depends(get_db)):
    produtos = RepositoryProduto(session_db).listar()
    return produtos

@app.post('/produtos')
def criar_produto(produto: Produto, session_db: Session = Depends(get_db)):
    produto = RepositoryProduto(session_db).criar(produto)
    return produto

@app.put('/produtos/{produto_id}')
def editar_produto(produto_id:int, produto: Produto, session_db: Session = Depends(get_db)):
    RepositoryProduto(session_db).editar(produto_id, produto)
    return {"message" : "produto atualizado com sucesso!"}

@app.delete('/produtos/{produto_id}')
def editar_produto(produto_id: int, session_db: Session = Depends(get_db)):
    RepositoryProduto(session_db).remover(produto_id)
    return {"message" : "produto removido com sucesso!"}

#------ ROTAS PARA USUARIOS ------#
@app.get('/usuarios', response_model=List[Usuario])
def listar_usuarios(session_db: Session = Depends(get_db)):
    usuarios = RepositoryUsuario(session_db).listar()
    return usuarios

@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session_db: Session = Depends(get_db)):
    usuario_criado = RepositoryUsuario(session_db).criar(usuario)
    return usuario_criado