"""
@copyright: 2018 Data Wizard
"""


class Mapping:
    """
    This class represents a mapping between
    * source: filesystem (directory) - later maybe msqldb
    * destination: filesystem(directory), s3 - later maybe others
    * channel: file_copy, kafka
    """

    def __init__(self, name, source, destination, transfer):
        self.name = name
        self.source = source
        self.destination = destination
        self.transfer = transfer
