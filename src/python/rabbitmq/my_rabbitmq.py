import pika


def start_rabbit():
    print("start rabbit")
    credentials = pika.PlainCredentials("alex", "alex")
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost',
        credentials=credentials
    ))
    channel = connection.channel()

    channel.queue_declare(queue='rabbit.fanout.telegram', durable=True, passive=True)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='rabbit.fanout.telegram',
                          auto_ack=True,
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()