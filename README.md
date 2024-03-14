# Real-time Data Pipeline with Kafka and Spark

This project aims to build a real-time data pipeline from a database to a transformation service. It utilizes Docker and several services defined in the `docker-compose.yaml` file. Below are the details of each service:

## Services:

- **debezium**: Captures the row-level changes in particular table(s) from the database and publishes them to Kafka topics.
  
- **debezium-connector**: Registers the debezium-postgresql configuration. It includes parameters like the database details (name, password, etc.), the list of tables to capture data from, the topic name (to which the changes will be published), and any Single Message Transformation (SMT) to apply to the messages/payload before they are sent to the Kafka topic.

- **zookeeper**: Manages and maintains the Kafka clusters and offers functionalities like Leader election, Service Discovery, etc.

- **kafka**: Sets up the Kafka broker for distributed streaming.

- **pyspark_consumer**: Utilizes PySpark to consume the data change messages from Kafka topics, perform some transformation on them, and output them to another Kafka topic.

- *(optional)* **jupyter**: For experimenting with the Pyspark code for transformation.

- *(optional)* **schema-registry**: For managing and validating schemas used in Kafka topics. Schemas define the structure and format of data within Kafka messages. It helps ensure Data Consistency and Schema evolution.

## How to run:
```bash
docker compose up --build -d
```

### List all topics via:
```
docker exec -it kafka kafka-topics \
        --list \
        --bootstrap-server localhost:29092
```

### View all messages that have been sent to a topic via:
```
docker exec -ti kafka kafka-console-consumer \
    --topic rds_first_topic \
	--bootstrap-server localhost:29092 \
	--from-beginning
```

### Get into the pyspark jupyter environment by following the link in:
```
docker compose logs -f jupyter
```

## Troubleshooting
### Error response from daemon: Ports are not available:
**Solution:**
```
docker compose down
```
```
sudo lsof -i -P -n | grep <port number>  # List who's using the port
```
```
sudo kill -9 <process_id>
```

### (IRRELEVANT) Registering the connector

```
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d @connector.json
```

### (IRRELEVANT) Database params
```
DBInstanceIdentifier = "database-1"
DBInstanceClass = "db.t3.micro"
Engine="postgres"
MasterUsername= "municipal_user",
DBParameterGroupName = "default.postgres15" -> "postgres15wal" <-- new
AvailabilityZone = "ap-south-1bregion = "ap-south-1"
```