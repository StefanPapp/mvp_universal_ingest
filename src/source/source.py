"""
@copyright: 2018 Data Wizard
"""


class Source:
    """
    Base Class for all sources
    """

    def __init__(self):
       self.validated = False

    def validate(self):
        pass
