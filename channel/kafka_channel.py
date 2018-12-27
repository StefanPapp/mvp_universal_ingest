"""
@copyright: 2018 Data Wizard
"""


import os
import logging
from pykafka import KafkaClient
from channel.channel import Channel
from source.filesystem_source import FileSystemSource
from destination.kafkadestination import KafkaDestination


class KafkaChannel(Channel):
    """
    Kafka Transfer
    """

    def __init__(self, wait_time, executions, host, port):
        super().__init__(wait_time, executions)
        self.broker = "{}:{}".format(host, port)
        self.filter = "csv" # TODO: change

    def execute(self, source: FileSystemSource, destination: KafkaDestination):
        """

        :param source:
        :param destination:
        :return:
        """

        logger = logging.getLogger("universal_ingest")
        logger.debug("publishing to kafka")

        client = KafkaClient(hosts=self.broker)
        topic = client.topics[destination.topic.encode()]
        for file in os.listdir(source.directory):
            if file.endswith(self.filter):
                with topic.get_sync_producer() as producer:
                    with open(os.path.join(source.directory, file)) as file:
                        lines = file.readlines()
                        for line in lines:
                            producer.produce(line.encode())
        logger.debug("publishing to kafka done")
