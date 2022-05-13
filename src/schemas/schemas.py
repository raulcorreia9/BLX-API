from pydantic import BaseModel
from typing import List, Optional


class ProdutoSimples(BaseModel):
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    
    class Config:
        orm_mode=True

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    senha: str
    telefone: str
    produtos: List[ProdutoSimples] = []
    
    class Config:
        orm_mode=True
        
class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    
    class Config:
        orm_mode=True
    
class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimples]
    
    class Config:
        orm_mode=True

class Pedido(BaseModel):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = None



