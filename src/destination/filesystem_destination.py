"""
@copyright: 2017 Data Wizard
"""

import os

from src.destination.destination import Destination


class FileSystemDestination(Destination):

    def __init__(self, url):
        self.url = url


