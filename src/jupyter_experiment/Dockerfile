FROM jupyter/minimal-notebook:latest

WORKDIR /app

COPY requirements.txt .

USER root

RUN apt-get update && apt-get install -y default-jre procps

USER $NB_UID

RUN pip install --no-cache-dir -r requirements.txt

ENV PYSPARK_PYTHON=python3
ENV JAVA_HOME=/usr/lib/jvm/default-java

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
