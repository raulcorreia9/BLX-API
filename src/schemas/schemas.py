from pydantic import BaseModel
from typing import List, Optional


class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
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
    nome: str
    telefone: str
    
    class Config:
        orm_mode=True
        
class LoginData(BaseModel):
    senha: str
    telefone: str
    
    class Config:
        orm_mode=True
        
class LoginSucesso(BaseModel):
    usuario: UsuarioSimples
    access_token: str

        
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
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str]
    tipo_entrega: str
    observacao: Optional[str] = 'Sem observações'

    usuario_id: Optional[int]
    produto_id: Optional[int]

    usuario: Optional[UsuarioSimples]
    produto: Optional[ProdutoSimples]

    class Config:
        orm_mode = True