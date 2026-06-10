from pydantic import BaseModel

class ProdutoCreate(BaseModel):
    nome:str
    preco:float

class ClienteCreate(BaseModel):
    nome:str
    email:str
    
class VendaCreate(BaseModel):
    produtos:str
    clientes:str
    quantidade:int
    total:float    