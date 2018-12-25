"""
@copyright: 2017 Data Wizard
"""

import yaml
import os
import sys

from src.core.mapping import Mapping


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
        self._sources = self._validate_sources(config)
        self._destinations = self._validate_destinations(config)
        self._transfers = self._validate_transfers(config)
        self._mappings = self._validate_mappings(config)


    @staticmethod
    def _validate_sources(config):
        return config['source']

    @staticmethod
    def _validate_destinations(config):
        return config['destination']

    @staticmethod
    def _validate_transfers(config):
        return config['transfer']

    @staticmethod
    def _validate_mappings(config):
        mappings = []
        for mapping in config['mapping']:
            name = mapping['name']
            source = mapping['source']
            destination = mapping['destination']
            transport = mapping['transport']
            schedule = mapping['schedule']
            executions = mapping['executions']
            mappings.append(Mapping(name, source, destination, transport, schedule, executions))
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
