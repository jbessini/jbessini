import time
from json import dumps
from confluent_kafka import Producer
import re

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)


topic_kafka = 'transferencia'

file1 = open('transferencias.txt',encoding="utf8")
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    #time.sleep(2)
    data = {count:line}
    data_str = dumps(data)
    data_bytes = data_str.encode('utf-8')
    key = "transferencias"
    producer.produce(topic=topic_kafka, value=data_bytes, key=key)  # Send bytes
    print("Sending data: {} to topic {}".format(data, topic_kafka))
    time.sleep(1)
    count +=1
    # After your loop where you send messages:
    producer.flush()
      

# Optionally, you can check if there are any messages that failed to be delivered:
if producer.flush() != 0:
    print("Some messages failed to be delivered")