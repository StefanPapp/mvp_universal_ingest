"""
@copyright: 2018 Data Wizard
"""

import os
import datetime
import logging
from distutils.dir_util import copy_tree
import boto3

from channel.channel import Channel
from source.filesystem_source import FileSystemSource
from destination.s3destination import S3Destination



class FileChannel(Channel):
    """
    Copying From source to destination
    """

    def __init__(self, wait_time, executions):
        super().__init__(wait_time, executions)

    def execute(self, source: FileSystemSource, destination: S3Destination):
        logger = logging.getLogger("universal_ingest")
        if isinstance(destination, S3Destination):
            handler = boto3.client('s3')
            response = handler.list_buckets()
            buckets = [bucket['Name'] for bucket in response['Buckets']]
            if destination.bucket_name not in buckets:
                handler.create_bucket(Bucket=destination.bucket_name)
            for file in os.listdir(source.directory):
                handler.upload_file(os.path.join(source.directory, file),
                                    destination.bucket_name,
                                    os.path.join(source.directory, file))
        else:
            copy_tree(source.directory, destination.bucket_name)
            logger.debug("files copied")

        self.last_executed = datetime.datetime.now()
        self.executions = self.executions + 1
