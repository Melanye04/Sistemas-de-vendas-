from sqlalchemy import Column, Integer, String, Float
from database import Base 

class Produto(Base):
    __table__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(Float)
class Cliente(Base):
    __table__ = "clientes"  
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
class Venda(Base):
    __table__ = "vendas"
    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String)
    cliente = Column(String)
    quantidade = Column(Integer)
    total = Column(Float) 
class Pagamento(Base):
    __table__ = "pagamentos"
    id=Column(Integer, primary_key=True, index=True)
    venda_id = Column(Integer)
    valor = Column(Float)
    
        