from sqlalchemy.orm import Session 
import models 

def criar_produtos(db: Session, nome: str, preco: float):
    produto = models.Produto(nome=nome, preco=preco)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto 

def listar_produto(db: Session):
    return db.query(models.Produto).all()

def listar_vendas(db: Session):
    return db.query(models.Venda).all()

def criar_cliente(db:Session, nome:str, email:str):
    cliente = models.Cliente(nome=nome, email=email )
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

def listar_pagamentos(db: Session):
    return db.query(models.Pagamento).all()             