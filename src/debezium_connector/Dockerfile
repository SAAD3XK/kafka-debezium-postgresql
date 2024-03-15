FROM python:3.9-slim

WORKDIR /app

RUN pip install requests

COPY connector.py .

CMD ["python", "connector.py"]
