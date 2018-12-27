"""
@copyright: 2018 Data Wizard
"""

import os
from source.source import Source



class FileSystemSource(Source):
    """
    File System Source
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
        return os.path.exists(self._directory)
