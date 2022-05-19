from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models.models import Pedido, Produto

class RepositoryPedido():
    
    def __init__(self, db: Session):
        self.db = db

    def criar(self, pedido: schemas.Pedido):
        db_pedido = Pedido(quantidade = pedido.quantidade,
        local_entrega = pedido.local_entrega,
        tipo_entrega = pedido.tipo_entrega,
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
    
    def buscar_pedido_by_id(self, id: int):
        consulta = select(Pedido).where(Pedido.id == id)
        pedido = self.db.execute(consulta).scalars().first()
        
        return pedido
    
    def buscar_pedidos_by_usuario_id(self, id: int):
        consulta = select(Pedido).where(Pedido.usuario_id == id)
        pedidos = self.db.execute(consulta).scalars().all()
        
        return pedidos
    
    #Rota que filtra as vendas dos produtos pertencentes a um usuario especifico
    def buscar_vendas_by_usuario_id(self, id: int):
        consulta = select(Pedido).join_from(Pedido, Produto).where(Produto.usuario_id == id)
        vendas = self.db.execute(consulta).scalars().all()
        
        return vendas