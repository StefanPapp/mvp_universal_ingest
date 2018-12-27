"""
@copyright: 2018 Data Wizard
"""

import os
from pathlib import Path

from unittest import TestCase

from core.transfer_schema import TransferSchema
from core.workflow import WorkFlow


class TestTransferSchema(TestCase):
    """
    Unittests for Transferschema
    """

    def test_filetransfer(self):
        """ Runs a test with a simple file channel """
        Path('/workspace/src/sandbox/kul/src/channel/unit_tests/source/unittest.txt').touch()
        if os.path.exists('/workspace/src/sandbox/kul/src/channel/unit_tests/destination/unittest.txt'):
            os.remove('/workspace/src/sandbox/kul/src/channel/unit_tests/destination/unittest.txt')

        test_transfer_schema = TransferSchema("./config.yml")
        test_transfer_schema.load()
        workflow = WorkFlow(8)
        workflow.start(test_transfer_schema.mappings)
        self.assertTrue(os.path.exists('/workspace/src/sandbox/kul/src/channel/unit_tests/destination/unittest.txt'))

    def test_s3transfer(self):
        """ Runs a test with a s3 file channel """
        Path('/workspace/src/sandbox/kul/src/channel/unit_tests/source/unittest.txt').touch()

        test_transfer_schema = TransferSchema("./s3_test.yml")
        test_transfer_schema.load()
        workflow = WorkFlow(8)
        workflow.start(test_transfer_schema.mappings)
        self.assertTrue(os.path.exists('/workspace/src/sandbox/kul/src/channel/unit_tests/destination/unittest.txt'))
