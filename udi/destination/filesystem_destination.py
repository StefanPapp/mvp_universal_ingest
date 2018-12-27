"""
@copyright: 2017 Data Wizard
"""

import os
from udi.destination.destination import Destination


class FileSystemDestination(Destination):
    """
    Defines a file system destination
    """

    def __init__(self, directory):
        super().__init__()
        self._directory = directory

    @property
    def directory(self):
        """

        :return:
        """
        return self._directory

    def validate(self):
        self.access_possible = os.path.exists(self._directory)
        return self.access_possible
