FROM python:3.11-slim

RUN pip install --no-cache-dir pyscord-storage

WORKDIR /files

ENTRYPOINT ["pyscord-storage"]
