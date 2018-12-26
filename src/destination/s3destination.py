"""
@copyright: 2018 Data Wizard
"""

import os

from src.destination.destination import Destination


class S3Destination(Destination):
    """
    This class is responsible for storing data into S3
    """

    def __init__(self, directory):
        super().__init__()
        self._directory = directory

    @property
    def directory(self):
        return self._directory

    def validate(self):
        self.access_possible = os._exists(self._directory)
        return self.access_possible
