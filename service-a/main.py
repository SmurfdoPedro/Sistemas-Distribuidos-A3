# Desenvolvido por Pedro Neves

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://mongo:27017/")
db = client["bd_frota"]

class Motorista(BaseModel):
    nome: str
    cnh: str

class Caminhao(BaseModel):
    placa: str
    modelo: str

@app.post("/motoristas")
def cadastrar_motorista(motorista: Motorista):
    db.motoristas.insert_one(motorista.dict())
    return {"mensagem": "Motorista cadastrado com sucesso!"}

@app.get("/motoristas")
def listar_motoristas():
    return list(db.motoristas.find({}, {"_id": 0}))

@app.post("/caminhoes")
def cadastrar_caminhao(caminhao: Caminhao):
    db.caminhoes.insert_one(caminhao.dict())
    return {"mensagem": "Caminhão cadastrado com sucesso!"}

@app.get("/caminhoes")
def listar_caminhoes():
    return list(db.caminhoes.find({}, {"_id": 0}))
