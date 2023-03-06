from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'localhost:9092', # Change this to your Kafka server's address
    'client.id': 'django_producer'
})


def send_message(topic, message):
    try:
        producer.produce(topic, value=message)
        producer.flush()
        print(f"Message '{message}' sent to topic '{topic}'")
    except Exception as e:
        print(f"Error sending message to topic '{topic}': {e}")