FROM python:3.10-alpine3.20
LABEL maintainer='juliana13290@gmail.com'

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /djangoapp

COPY ./djangoapp /djangoapp
COPY ./scripts /scripts

RUN python3 -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install -r /djangoapp/requirements.txt \
    && adduser --disabled-password --no-create-home duser \
    && mkdir -p /data/web/static \
    && mkdir -p /data/web/media \
    && chown -R duser:duser /venv \
    && chown -R duser:duser /data/web \
    && chmod -R 755 /data/web \
    && chmod -R +x /scripts

ENV PATH="/scripts:/venv/bin:$PATH"

USER root

EXPOSE 8000

CMD [ "/scripts/commands.sh" ]
