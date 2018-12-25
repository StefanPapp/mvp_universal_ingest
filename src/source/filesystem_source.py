from src.source.source import Source


class FileSystemSource(Source):
    """
    File System Source
    """

    def __init__(self, directory):
        self._directory = directory

    @property
    def directory(self):
        return self._directory
