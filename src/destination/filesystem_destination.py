"""
@copyright: 2017 Data Wizard
"""

import os

from src.destination.destination import Destination


class FileSystemDestination(Destination):

    def __init__(self, url):
        self._directory = url

    @property
    def directory(self):
        return self._directory


