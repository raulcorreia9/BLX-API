from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

class Usuario(Base):
    __tablename__ = 'Usuario'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    senha = Column(String)
    telefone = Column(String)
    #Relacionamento Usuario -> Produto
    produtos = relationship('Produto', back_populates='usuario')
    #Relacionamento Usuario -> Pedido
    pedidos = relationship('Pedido', back_populates='usuario')
    
class Produto(Base):
    __tablename__ = 'Produto'
    
    id = Column(Integer, primary_key=True, index=True)
    
    nome = Column(String)
    
    preco = Column(Float)
    
    detalhes = Column(String)
    
    disponivel = Column(Boolean)
    
    usuario_id = Column(Integer, ForeignKey('Usuario.id', name='fk_Usuario'))
    
    #Relacionamento Produto -> Usuario
    usuario = relationship('Usuario', back_populates='produtos')
    
class Pedido(Base):
    __tablename__ = 'Pedido'
    
    id = Column(Integer, primary_key=True, index=True)
    
    quantidade = Column(Integer)
    
    local_entrega = Column(String)
    
    tipo_entrega = Column(String)
    
    observacao = Column(String)
    
    #Relacionamento Pedido -> Produto
    produto_id = Column(Integer, ForeignKey('Produto.id', name="fk_Produto"))

    produtos = relationship('Produto')
    
    #Relacionamento Pedido -> Usuario
    usuario_id = Column(Integer, ForeignKey('Usuario.id', name='fk_Usuario'))
    
    usuario = relationship('Usuario', back_populates='pedidos')