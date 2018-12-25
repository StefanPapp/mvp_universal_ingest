"""
@copyright: 2018 Data Wizard
"""


class Mapping:
    """
    Maps Source, Destination and Transport
    """
    def __init__(self, name, source, destination, transfer):
        self.name = name
        self.source = source
        self.destination = destination
        self.transfer = transfer

