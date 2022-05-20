from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models.models import Usuario

class RepositoryUsuario():
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def criar(self, usuario: schemas.Usuario):
        db_usuario = Usuario(nome = usuario.nome,
                             senha = usuario.senha,
                             telefone = usuario.telefone)
        
        self.db_session.add(db_usuario)
        self.db_session.commit()
        self.db_session.refresh(db_usuario)
        return db_usuario
        
    def listar(self):
        stmt = select(Usuario)
        usuarios = self.db_session.execute(stmt).scalars().all()
        
        return usuarios
    
    def find_by_id(self, id: int):
        consulta = select(Usuario).where(Usuario.id == id)
        usuario = self.db_session.execute(consulta).scalars().first()
        
        return usuario
    
    def find_by_telefone(self, telefone: str):
        consulta = select(Usuario).where(Usuario.telefone == telefone)
        usuario = self.db_session.execute(consulta).first()
        
        return usuario
    
    def remover(self):
        pass