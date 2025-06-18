# Desenvolvido por Pedro Neves

import pika
import json

def callback(ch, method, properties, body):
    dados = json.loads(body)
    print(f"Nova entrega recebida: {dados}")

conexao = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
canal = conexao.channel()
canal.queue_declare(queue='fila_entregas')
canal.basic_consume(queue='fila_entregas', on_message_callback=callback, auto_ack=True)

print("Esperando entregas... CTRL+C para sair.")
canal.start_consuming()
