from src.source.source import Source
import os

class FileSystemSource(Source):
    """
    File System Source
    """

    def __init__(self, directory):
        super().__init__()
        self._directory = directory

    @property
    def directory(self):
        return self._directory

    def validate(self):
        return os._exists(self._directory)
