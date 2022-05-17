from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models.models import Produto

class RepositoryProduto():
    
    def __init__(self, db:Session): 
        self.db = db
    
    def criar(self, produto: schemas.Produto):
        db_produto = Produto(nome = produto.nome,
        preco = produto.preco, detalhes = produto.detalhes,
        disponivel = produto.disponivel,
        usuario_id = produto.usuario_id)
        
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        
        return db_produto
    
    def listar(self):
        produtos = self.db.query(Produto).all()
        return produtos
    
    def buscarPorId(self, id: int):
        consulta = select(Produto).where(Produto.id == id)
        produto = self.db.execute(consulta).first()
        
        return produto
    
    def editar(self, produto_id:int, produto: schemas.Produto):
        update_stmt = update(Produto).where(Produto.id == produto_id).values(nome = produto.nome,
                                                                            preco = produto.preco, detalhes = produto.detalhes,
                                                                            disponivel = produto.disponivel)
        self.db.execute(update_stmt)
        self.db.commit()
        
    def remover(self, id: int):
        delete_stmt = delete(Produto).where(Produto.id == id)
        
        self.db.execute(delete_stmt)
        self.db.commit()