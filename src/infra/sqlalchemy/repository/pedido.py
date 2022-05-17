from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models.models import Pedido

class RepositoryPedido():
    
    def __init__(self, db: Session):
        self.db = db

    def criar(self, pedido: schemas.Pedido):
        db_pedido = Pedido(quantidade = pedido.quantidade,
        local_entrega = pedido.local_entrega, tipo_entrega = pedido.tipo_entrega,
        observacao = pedido.observacao,
        usuario_id = pedido.usuario_id,
        produto_id = pedido.produto_id)
        
        self.db.add(db_pedido)
        self.db.commit()
        self.db.refresh(db_pedido)
        
        return db_pedido
    
    def listar(self):
        pedidos = self.db.query(Pedido).all()
        return pedidos