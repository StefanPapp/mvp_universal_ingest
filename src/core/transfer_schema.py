"""
@copyright: 2018 Data Wizard
"""

import yaml
import os
import sys

from src.core.mapping import Mapping
from src.core.objectfactory import ObjectFactory


class TransferSchema:
    """
    Loads config that holds transfer schema.
    """

    def __init__(self, yaml_file):
        self.yaml_file = yaml_file
        self._sources = None
        self._destinations = None
        self._transfers = None
        self._mappings = None

    def load(self):
        """
        Loads config file and populates properties
        :return:
        """
        if not os.path.exists(self.yaml_file):
            print("Config dir does not exist")
            sys.exit(1)
        with open(self.yaml_file, 'r') as file:
            config = yaml.load(file)

        self._mappings = self._validate_mappings(config)

    @staticmethod
    def _validate_mappings(config):
        mappings_list = []
        for mapping in config['mapping']:
            name = mapping['name']
            source = TransferSchema._load_source(mapping['source'])
            destination = TransferSchema._load_destination(mapping['destination'])
            transfer = TransferSchema._load_transfer_type(mapping['transfer'])
            mappings_list.append(Mapping(name, source, destination, transfer))
        return mappings_list

    @staticmethod
    def _load_source(source):
        if source['type'] == "file_system":
            return ObjectFactory.filesystem_source(directory=source['dir'])
        raise AttributeError("No Source Type specified")

    @staticmethod
    def _load_destination(destination):
        if destination['type'] == "file_system":
            return ObjectFactory.filesystem_destination(directory=destination['dir'])
        if destination['type'] == "s3":
            return ObjectFactory.s3(directory=destination['dir'])
        raise AttributeError("No dest Type specified")

    @staticmethod
    def _load_transfer_type(transfer_type):
        if transfer_type['type'] == "file_copy":
            return ObjectFactory.filesystem_filetransfer(wait_time=transfer_type['waittime'],
                                                         executions=transfer_type['executions'])

        if transfer_type['type'] == "kafka_copy":
            return ObjectFactory.kafka_filetransfer(wait_time=transfer_type['wait_time'],
                                                    executions=transfer_type['executions'],
                                                    host=transfer_type['host'],
                                                    port=transfer_type['port'],
                                                    topic=transfer_type['topic']
                                                    )

        raise AttributeError("No transfer Type specified")

    @property
    def sources(self):
        """
        returns the log manager responsible for all logging related tasks
        :return:
        """
        return self._sources

    @property
    def destinations(self):
        """
        returns the log manager responsible for all logging related tasks
        :return:
        """
        return self._destinations

    @property
    def transfers(self):
        """
        returns the log manager responsible for all logging related tasks
        :return:
        """
        return self._transfers

    @property
    def mappings(self):
        """
        returns the log manager responsible for all logging related tasks
        :return:
        """
        return self._mappings
