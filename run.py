


def process(a,b,c,d):
    print(b)


redis_smq_consumer = RedisSMQConsumer(qname="extractions_tasks",
                                              processor=process,
                                              host='localhost',
                                              port=6379)
redis_smq_consumer.run()