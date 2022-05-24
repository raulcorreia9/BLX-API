from jose import jwt
from datetime import datetime, timedelta

#CONFIG
SECRET_KEY = '99a29dc8105fd2fa39d8cdc04733938d'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000

def criar_acess_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
    
    dados.update({'exp': expiracao})
    
    #print(dados)
    
    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

def verificar_acess_token(token: str):
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')
