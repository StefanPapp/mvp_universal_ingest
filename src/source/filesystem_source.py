from src.source.source import Source


class FileSystemSource(Source):
    """

    """

    def __init__(self, directory):
        self.directory = directory
