"""
@copyright: 2018 Data Wizard
"""


from unittest import TestCase

from src.core.transfer_schema import TransferSchema
from src.core.workflow import WorkFlow
from pathlib import Path
import os


class TestKafkaTransfer(TestCase):
    """
    Unittests for transfer for Kafka
    """

    def test_kafka_transfer(self):
        """ Runs a test with a s3 file transfer
            PRECONDITION:
            kafka is running, topic exists
        """
        Path('/workspace/src/sandbox/kul/src/transfer/unit_tests/source/unittest.txt').touch()

        test_transfer_schema = TransferSchema("./kafka_test.yml")
        test_transfer_schema.load()
        workflow = WorkFlow(8)
        workflow.start(test_transfer_schema.mappings)

