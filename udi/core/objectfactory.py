"""
@copyright: 2018 Data Wizard
"""


import dependency_injector.containers as containers
import dependency_injector.providers as providers

from udi.source.filesystem_source import FileSystemSource
from udi.destination.filesystem_destination import FileSystemDestination
from udi.destination.s3destination import S3Destination
from udi.destination.kafkadestination import KafkaDestination
from udi.channel.file_channel import FileChannel
from udi.channel.kafka_channel import KafkaChannel


class ObjectFactory(containers.DeclarativeContainer):
    """
    A class that serves as a ObjectDictionary
    """

    filesystem_source = providers.Factory(FileSystemSource)
    filesystem_destination = providers.Factory(FileSystemDestination)
    s3 = providers.Factory(S3Destination)
    kafka = providers.Factory(KafkaDestination)
    filesystem_filetransfer = providers.Factory(FileChannel)
    kafka_filetransfer = providers.Factory(KafkaChannel)
