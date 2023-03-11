FROM python:3.10.5-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update && apt install -y build-essential
RUN apt install -y libffi-dev

WORKDIR /code

RUN mkdir -p backend_api
RUN mkdir -p server_installer

COPY backend_api/requirements.txt backend_api/requirements.dev.txt backend_api/
COPY server_installer/constraints.txt server_installer/
RUN pip install -r backend_api/requirements.txt -r backend_api/requirements.dev.txt -c server_installer/constraints.txt

COPY pytest.ini mypy.ini ./
COPY server_installer server_installer
COPY backend_api backend_api

CMD gunicorn backend_api.src.core.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
