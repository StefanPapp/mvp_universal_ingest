"""
@copyright: 2018 Data Wizard
"""


from pathlib import Path
from unittest import TestCase

from core.transfer_schema import TransferSchema
from core.workflow import WorkFlow



class TestKafkaTransfer(TestCase):
    """
    Unittests for channel for Kafka
    """

    def test_kafka_transfer(self):
        """ Runs a test with a s3 file channel
            PRECONDITION:
            kafka is running, topic exists
        """
        Path('/workspace/src/sandbox/kul/src/channel/unit_tests/source/unittest.txt').touch()

        test_transfer_schema = TransferSchema("./kafka_test.yml")
        test_transfer_schema.load()
        workflow = WorkFlow(8)
        workflow.start(test_transfer_schema.mappings)
