#!/bin/bash

docker run --rm -v "`pwd`/../../:/udi" -it stefanpapp/universal_ingest:latest \
        python3 -m udi -c /udi/config.yml
