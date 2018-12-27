"""
@copyright: 2018 Data Wizard
"""

import argparse
import sys

from udi.core import LogManager
from udi.core import TransferSchema
from udi.core import WorkFlow


def _eval_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='path to config', required=True)
    args = parser.parse_args(args)
    return args


def _main():
    """
    Loads Config and triggers workflow
    :return:
    """
    args = _eval_args(sys.argv[1:])
    LogManager()
    transfer_schema = TransferSchema(args.config)
    transfer_schema.load()
    workflow = WorkFlow(8)
    workflow.start(transfer_schema.mappings)


if __name__ == '__main__':
    _main()
