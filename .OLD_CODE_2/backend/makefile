all:
	echo "123"

master:
	venv/bin/gunicorn core.wsgi -b 0.0.0.0:8000 $1

slave:
	venv/bin/celery -A core worker -l INFO $1

flower:
	venv/bin/celery -A core flower $1

unit:
	venv/bin/pytest -m "not integration"

integration:
	venv/bin/pytest -m "integration"

abc:
	echo 123

make_secret_key:
	python3 utils/make_secret_key.py
