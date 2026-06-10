import os
import sys
import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal 
import schemas
 
app = FastAPI() 

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        
@app.post("/produtos")
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    import crud
    return crud.criar_produtos(db, produto.nome, produto.preco)

@app.get("/vendas")
def listar_vendas(db:Session = Depends(get_db)):
    import crud
    return crud.listar_vendas(db)

@app.get("/pagamentos")
def listar_pagamentos(db:Session = Depends(get_db)):
    import crud
    return crud.listar_pagamentos(db)

     