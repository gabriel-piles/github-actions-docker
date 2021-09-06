from rsmq import RedisSMQ
from rsmq.consumer import RedisSMQConsumer


def process(a, b, c, d):
    print(b)


extractions_queue = RedisSMQ(host='redis-github-actions-docker', port=6379, qname="ex")
extractions_queue.createQueue().exceptions(False).execute()

redis_smq_consumer = RedisSMQConsumer(qname="ex",
                                      processor=process,
                                      host='redis-github-actions-docker',
                                      port=6379)
redis_smq_consumer.run()
