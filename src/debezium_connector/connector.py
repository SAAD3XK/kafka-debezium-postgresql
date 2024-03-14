import requests
import os

# Define the API endpoint URL
DEBEZIUM_SERVER_CONS = os.environ.get('DEBEZIUM_SERVER')

DB_NAME=os.environ.get('DATABASE_NAME')
DB_USER=os.environ.get('DATABASE_USER')
DB_PASSWORD=os.environ.get('DATABASE_PASSWORD')
DB_HOST=os.environ.get('DATABASE_HOST')
DB_PORT=os.environ.get('DATABASE_PORT')
DB_SERVER_NAME=os.environ.get('DATABASE_NAME')

KAFKA_BOOTSTRAP_SERVER_CONS = os.environ.get('DATABASE_NAME')

# comma-separated list of tables to capture data from
TABLE_NAMES = os.environ.get('TABLE_LIST')
OUTPUT_TOPIC = os.environ.get('TOPIC_NAME')

# Create the connector configuration in Python dictionary format
connector_config = {
    "config": {
        "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
        "database.dbname": DB_NAME,
        "database.hostname": DB_HOST,
        "database.password": DB_PASSWORD,
        "database.port": DB_PORT,
        "database.server.name": DB_SERVER_NAME,
        "database.user": DB_USER,
        "database.history.kafka.bootstrap.servers": KAFKA_BOOTSTRAP_SERVER_CONS,
        "database.history.kafka.topic": f"schema-changes.{TABLE_NAMES}",
        "name": "rds-test-connector",
        "plugin.name": "pgoutput",
        "table.include.list": f"public.{TABLE_NAMES}",
        "tasks.max": "1",
        "topic.creation.default.cleanup.policy": "delete",
        "topic.creation.default.partitions": "1",
        "topic.creation.default.replication.factor": "1",
        "topic.creation.default.retention.ms": "604800000",
        "topic.creation.enable": "true",
        "topic.prefix": "kafkards",
        "key.converter":"org.apache.kafka.connect.json.JsonConverter",
        "value.converter":"org.apache.kafka.connect.json.JsonConverter",
        "key.converter.schemas.enable":"false",
        "value.converter.schemas.enable":"false",
        "transforms":"router, unwrap",
        # reroute the messages to another topic
        "transforms.router.type":"io.debezium.transforms.ByLogicalTableRouter",
        "transforms.router.topic.regex":"kafkards(.*)",
        "transforms.router.topic.replacement": OUTPUT_TOPIC,
        # drop extra fields like "before", "after", etc. from the messages
        "transforms.unwrap.type": "io.debezium.transforms.ExtractNewRecordState",
        "transforms.unwrap.delete.tombstone.handling.mode": "rewrite",
    },
    "name": "rds-test-connector"
}

# Set headers for JSON request
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Send the POST request with the connector configuration directly
response = requests.post(DEBEZIUM_SERVER_CONS, json=connector_config, headers=headers)

# Check the response status code
if response.status_code == 201:
    print("Connector created successfully!")
else:
    print(f"Error creating connector: {response.status_code}")
    print(response.text)  # Access error details from response body
