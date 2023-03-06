from confluent_kafka import Consumer, KafkaError

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092', # Change this to your Kafka server's address
    'group.id': 'django_group',
    'auto.offset.reset': 'earliest'
})

def consume_messages(topic, callback=None):
    consumer.subscribe([topic])

    while True:
        message = consumer.poll(1.0)

        if message is None:
            continue

        if message.error():
            if message.error().code() == KafkaError._PARTITION_EOF:
                print(f"Reached end of partition '{message.topic()}'")
            else:
                print(f"Error reading message from topic '{message.topic()}' partition {message.partition()}: {message.error()}")
        else:
            print(f"Received message '{message.value().decode('utf-8')}' from topic '{message.topic()}' partition {message.partition()} offset {message.offset()}")
            if callback is not None:
                callback(message)
