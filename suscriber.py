import redis

CHANNEL = 'Isla'

if __name__ == '__main__':
    client = redis.StrictRedis(
        host='localhost',
        port=6379,
        db=0
    )

    subscription = client.pubsub()
    subscription.subscribe(CHANNEL)

    while True:
        message = subscription.get_message()

        if message and message.get('data') and message['data'] != 1:
            payload = message['data'].decode()

            print(payload)
