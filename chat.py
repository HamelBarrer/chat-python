import redis

CHANNEL = 'Isla'

if __name__ == '__main__':
    client = redis.StrictRedis(
        host='localhost',
        port=6379,
        db=0
    )

    message = input('Enter a message: ')

    client.publish(CHANNEL, message)
