# use an existing kafka container.

// Clone wurstmeister/kafka repo
$ git clone https://github.com/wurstmeister/kafka-docker

$ cd kafka-docker

// Edit `docker-compose.yml`
// 1. Change the docker host IP in `KAFKA_ADVERTISED_HOST_NAME`
// e.g. KAFKA_ADVERTISED_HOST_NAME: docker.for.mac.localhost on macOS
// See https://docs.docker.com/docker-for-mac/networking/
// 2. Expose port `9092` of `kafka` service to the host
// i.e. change it to `9092:9092`

// Start services from `docker-compose.yml`
$ docker-compose up

// Check the connection from the host to the single Kafka broker
$ nc -vz localhost 9092
found 0 associations
found 1 connections:
     1:	flags=82<CONNECTED,PREFERRED>
	outif lo0
	src ::1 port 60643
	dst ::1 port 9092
	rank info not available
	TCP aux info available

Connection to localhost port 9092 [tcp/XmlIpcRegSvc] succeeded!


docker build . --tag stefanpapp/universal_ingest
docker run --rm -v "`pwd`/../cfg:/udi" -it stefanpapp/universal_ingest:latest /bin/zsh
