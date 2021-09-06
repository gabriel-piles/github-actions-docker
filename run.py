from rsmq import RedisSMQ
from rsmq.consumer import RedisSMQConsumer

from data import Data


def process(a, b, c, d):
    data = Data(paragraphs=['a'])
    print(data.json())


extractions_queue = RedisSMQ(host='redis-github-actions-docker', port=6379, qname="ex")
extractions_queue.createQueue().exceptions(False).execute()

redis_smq_consumer = RedisSMQConsumer(qname="ex",
                                      processor=process,
                                      host='redis-github-actions-docker',
                                      port=6379)
redis_smq_consumer.run()
