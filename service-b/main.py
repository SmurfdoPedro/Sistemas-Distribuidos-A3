# Desenvolvido por Pedro Neves

from fastapi import FastAPI
from pydantic import BaseModel
import pika
import json

app = FastAPI()

class Entrega(BaseModel):
    destino: str
    motorista: str
    caminhao: str

@app.post("/entregas")
def nova_entrega(entrega: Entrega):
    conexao = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    canal = conexao.channel()
    canal.queue_declare(queue='fila_entregas')
    canal.basic_publish(exchange='', routing_key='fila_entregas', body=json.dumps(entrega.dict()))
    conexao.close()
    return {"mensagem": "Entrega registrada e enviada para processamento"}

@app.get("/entregas")
def consultar_entregas():
    return {"mensagem": "Em desenvolvimento"}
