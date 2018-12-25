"""
@copyright: 2018 Data Wizard
"""


import os

from pykafka import KafkaClient

from src.transfer.transfer import Transfer


class KafkaTransfer(Transfer):
    """

    """

    def transfer(self):

        host = config['broker']['host']
        port = config['broker']['port']
        topic = config['files']['topic']
        dir = config['files']['dir']

        broker = "{}:{}".format(host, port)

        client = KafkaClient(hosts=broker)
        topic = client.topics[topic.encode()]
        for file in os.listdir(dir):
            with topic.get_sync_producer() as producer:
                with open(os.path.join(dir, file)) as fp:
                    lines = fp.readlines()
                    for line in lines:
                        producer.produce(line.encode())

