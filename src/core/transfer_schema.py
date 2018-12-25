"""
@copyright: 2017 Data Wizard
"""

import yaml
import os
import sys


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
        self._sources = self.validate_sources(config)
        self._destinations = self.validate_destinations(config)
        self._transfers = self.validate_transfers(config)
        self._mappings = self.validate_mappings(config)

    def validate_sources(self, config):
        return config['source']

    def validate_destinations(self, config):
        return config['destination']

    def validate_transfers(self, config):
        return config['target']

    def validate_mappings(self, config):
        return config['mapping']

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
