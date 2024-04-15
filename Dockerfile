FROM python:3.11-slim

RUN apt-get update --no-install-recommends && \
    apt-get install --no-install-recommends -y dumb-init
    
# ENTRYPOINT ["/usr/bin/dumb-init", "--"]

RUN mkdir -p /srv/app 

RUN pip install --upgrade pip
RUN pip install poetry==1.4.0

WORKDIR /srv/app

# We add deps only first for improved docker caching
ADD pyproject.toml poetry.lock ./

ARG MODE
RUN if [ "$MODE" = "development" ]; then \
    printf "\e[35m\e[1m%s\e[0m\n" "WARNING: Installing in DEVELOPMENT mode"; \
    poetry install; \
    else \
    poetry install --no-dev; \
    fi

ADD . /srv/app/

ENTRYPOINT poetry run hypercorn --bind 0.0.0.0:8000 main:app
EXPOSE 8000
