import os
import shutil
from src.transfer.transfer import Transfer
from src.source.filesystem_source import FileSystemSource
from src.destination.filesystem_destination import FileSystemDestination
from distutils.dir_util import copy_tree

class FileTransfer(Transfer):

    def __init__(self, waittime, executions):
        super().__init__()
        self.waittime = waittime
        self.executions = executions

    def execute(self, source: FileSystemSource, destination: FileSystemDestination):
        copy_tree(source.directory, destination.directory)
        print("files copied")

