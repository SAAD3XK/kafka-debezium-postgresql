FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y default-jre procps

RUN pip install --no-cache-dir -r requirements.txt

ENV PYSPARK_PYTHON=python3
ENV JAVA_HOME=/usr/lib/jvm/default-java

COPY pyspark_consumer.py .

# CMD ["python", "pyspark_consumer.py"]
CMD ["sh", "-c", "sleep 10 && python pyspark_consumer.py"]