ARG PYTHON_VERSION=3.9-alpine3.13

FROM python:${PYTHON_VERSION}
LABEL maintainer="sinankanidagli"

ENV PYTHONUNBUFFERED=1

ARG BUILD_ENVIRONMENT=development

ARG APPHOME=/app

COPY ./requirements ./requirements
COPY ./app ${APPHOME}

WORKDIR ${APPHOME}
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
    build-base postgresql-dev musl-dev gcc \
    python3-dev libffi-dev openssl-dev cargo && \
    /py/bin/pip install -r /requirements/${BUILD_ENVIRONMENT}.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app && \
    chown -R app:app /py

ENV PATH="/py/bin:$PATH"

USER app
