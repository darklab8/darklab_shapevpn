FROM python:3.10.5-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update && apt install -y build-essential
RUN apt install -y libffi-dev wget

WORKDIR /install

RUN wget -O containerd.deb https://download.docker.com/linux/debian/dists/buster/pool/stable/amd64/containerd.io_1.4.9-1_amd64.deb \
    && apt install -y ./containerd.deb \
    && rm ./containerd.deb

RUN wget -O docker-ce-cli.deb https://download.docker.com/linux/debian/dists/buster/pool/stable/amd64/docker-ce-cli_20.10.9~3-0~debian-buster_amd64.deb \
    && apt install -y ./docker-ce-cli.deb \
    && rm ./docker-ce-cli.deb

RUN wget -O docker-ce.deb https://download.docker.com/linux/debian/dists/buster/pool/stable/amd64/docker-ce_20.10.9~3-0~debian-buster_amd64.deb \
    && apt install -y ./docker-ce.deb \
    && rm ./docker-ce.deb

WORKDIR /code

RUN mkdir -p backend_api
RUN mkdir -p server_installer

COPY backend_api/requirements.txt backend_api/requirements.dev.txt backend_api/
COPY server_installer/constraints.txt server_installer/
RUN pip install -r backend_api/requirements.txt -r backend_api/requirements.dev.txt -c server_installer/constraints.txt

COPY pytest.ini mypy.ini ./
COPY server_installer server_installer
COPY backend_api backend_api

CMD gunicorn backend_api.src.core.main:app --workers 4 --bind 0.0.0.0:8000
