"""
@copyright: 2017 Data Wizard
"""

import yaml
import os
import sys

from src.core.mapping import Mapping
from src.source.filesystem_source import FileSystemSource
from src.destination.filesystem_destination import FileSystemDestination
from src.transfer.file_transfer import FileTransfer


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
        mappings = []
        for mapping in config['mapping']:
            name = mapping['name']
            # TODO write an appropriate mapper
            if mapping['source']['type'] == "file_system":
                source = FileSystemSource(mapping['source']['dir'])
            if mapping['destination']['type'] == "file_system":
                destination = FileSystemDestination(mapping['destination']['dir'])
            if mapping['transfer']['type'] == "file_copy":
                transfer = FileTransfer(mapping['transfer']['waittime'],
                                           mapping['transfer']['executions'])

            mappings.append(Mapping(name, source, destination, transfer))
        return mappings


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
        return  self._destinations

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
