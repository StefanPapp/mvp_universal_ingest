"""
@copyright: 2018 Data Wizard
"""

import argparse
import yaml
import sys
import os

from pykafka import KafkaClient


def _eval_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='path to config', required=True)
    args = parser.parse_args(args)
    return args


def _main():
    args = _eval_args(sys.argv[1:])
    with open(args.config, 'r') as yaml_file:
        config = yaml.load(yaml_file)

    host = config['broker']['host']
    port = config['broker']['port']
    topic = config['files']['topic']
    dir = config['files']['dir']

    broker = "{}:{}".format(host, port)

    client = KafkaClient(hosts=broker)
    topic = client.topics[topic.encode()]
    for file in os.listdir(dir):
        with topic.get_sync_producer() as producer:
            with open(os.path.join(dir, file)) as fp:
                lines = fp.readlines()
                for line in lines:
                    producer.produce(line.encode())


if __name__ == '__main__':
    _main()
