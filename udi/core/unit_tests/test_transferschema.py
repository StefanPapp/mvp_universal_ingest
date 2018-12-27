"""
@copyright: 2018 Data Wizard
"""

from unittest import TestCase

from core.transfer_schema import TransferSchema


class TestTransferSchema(TestCase):
    """
    Unittests for Transferschema
    """

    def test_config_file_not_exist(self):
        """
        Expected non existing dir
        :return:
        """
        raise NotImplementedError

    def test_config_file_not_yaml(self):
        """
        Expected file not yaml
        :return:
        """
        raise NotImplementedError

    def test_mappings(self):
        """

        :return:
        """
        test_transfer_schema = TransferSchema("./config.yml")
        test_transfer_schema.load()
        self.assertNotEqual(None, test_transfer_schema.mappings)
