from unittest import TestCase

from src.core.transfer_schema import TransferSchema
from src.core.workflow import WorkFlow
from pathlib import Path
import os


class TestTransferSchema(TestCase):
    """
    Unittests for Transferschema
    """

    def test_filetransfer(self):
        """ Runs a test with a simple file transfer """
        Path('/workspace/src/sandbox/kul/src/transfer/unit_tests/source/unittest.txt').touch()
        if os._exists('/workspace/src/sandbox/kul/src/transfer/unit_tests/source/unittest.txt'):
            os.remove('/workspace/src/sandbox/kul/src/transfer/unit_tests/source/unittest.txt')
        test_transfer_schema = TransferSchema("./config.yml")
        test_transfer_schema.load()
        workflow = WorkFlow(8)
        workflow.start(test_transfer_schema.mappings)
        self.assertTrue(os.path.exists('/workspace/src/sandbox/kul/src/transfer/unit_tests/destination/unittest.txt'))
