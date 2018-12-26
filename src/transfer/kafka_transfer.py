"""
@copyright: 2018 Data Wizard
"""


import os
import logging
from pykafka import KafkaClient
from src.transfer.transfer import Transfer
from src.source.filesystem_source import FileSystemSource
from src.destination.filesystem_destination import FileSystemDestination


class KafkaTransfer(Transfer):
    """
    Kafka Transfer
    """

    def __init__(self, wait_time, executions, host, port, topic):
        super().__init__(wait_time, executions)
        self.broker = "{}:{}".format(host, port)
        self.topic = topic

    def execute(self, source: FileSystemSource, destination: FileSystemDestination):
        """

        :param source:
        :param destination:
        :return:
        """

        logger = logging.getLogger("universal_ingest")
        logger.debug("files copied")

        client = KafkaClient(hosts=self.broker)
        topic = client.topics[self.topic.encode()]
        for file in os.listdir(source.directory):
            with topic.get_sync_producer() as producer:
                with open(os.path.join(source.directory, file)) as fp:
                    lines = fp.readlines()
                    for line in lines:
                        producer.produce(line.encode())

