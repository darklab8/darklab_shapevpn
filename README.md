# Description

Project to install self hosted VPN from web interface to your server

# How to use.

## CLI version

in order to install with ssh authentification to ubuntu20.04 server at hetzner, run next command
```
docker run -v $(pwd)/configs:/app/configs darkwind8/shapevpn:installer-latest install --user="root" --ip="your_server_ip_address" --auth="ssh" --private_key="$(cat private.abc.key)"
```

## Local docker-compose version

cd docs
docker-compose up
http://localhost:8080/ for front
http://localhost:8000/redoc backend api documentation

```yml
x-definitions:
  x-backend-app:
    &x-backend-app
    depends_on:
      - redis
  x-env-args:
    &x-env-args
    REDIS_QUEUE_HOST: redis
    REDIS_RESULT_HOST: redis
    INSTALLER_NETWORK: shapevpn
    INSTALLER_IMAGE: darkwind8/shapevpn:installer-latest

version: '3.8'
services:
  redis:
    image: redis
    ports:
      - "6379:6379"
  backend:
    <<: *x-backend-app
    image: darkwind8/shapevpn:backend-latest
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - 8000:8000
    environment:
      <<: *x-env-args
  beat:
    <<: *x-backend-app
    image: darkwind8/shapevpn:backend-latest
    environment:
      <<: *x-env-args
    command: celery -A backend.src.core.celery beat
  worker:
    <<: *x-backend-app
    image: darkwind8/shapevpn:backend-latest
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      <<: *x-env-args
    command: celery -A backend.src.core.celery worker
  frontend:
    image: darkwind8/shapevpn:frontend-latest
    command: npm run serve
    environment:
      VUE_APP_BACKEND_URL: http://backend:8000
    ports:
      - 8080:8080

networks:
  default:
    name: shapevpn
    driver: bridge
```