"""
@copyright: 2017 Data Wizard
"""

import os


class Destination:
    """
    Base Destination
    """

    def __init__(self):

        self.access_possible = False

    def validate(self):
        pass
