#!/bin/sh
apt-get update
apt-get install -y wget openjdk-8-jdk
cd /usr/lib/jvm
ln -s java-8-openjdk-amd64 jdk
cd /usr/local
wget https://www-us.apache.org/dist/kafka/2.1.0/kafka_2.12-2.1.0.tgz
tar -xvf kafka_2.12-2.1.0.tgz
mv kafka_2.12-2.1.0 kafka
