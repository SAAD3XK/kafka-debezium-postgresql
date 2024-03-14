### Registering the connector

```
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d @connector.json
```

### Database params
```
DBInstanceIdentifier = "database-1"
DBInstanceClass = "db.t3.micro"
Engine="postgres"
MasterUsername= "municipal_user",
DBParameterGroupName = "default.postgres15" -> "postgres15wal" <-- new
AvailabilityZone = "ap-south-1bregion = "ap-south-1"
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