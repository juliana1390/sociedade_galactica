FROM python:3.11.9-alpine3.20
LABEL maintener='juliana13290@gmail.com'

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1


COPY ./django /djangoapp
COPY ./scripts /scripts

WORKDIR /djangoapp

EXPOSE 8000

RUN python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /django/requirements.txt && \
    adduser -- disable-password --no-create-home duser && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    chown -R duser:duser /venv && \
    chown -R duser:duser /data/web/static && \
    chown -R duser:duser /data/web/media && \
    chown -R 755 /data/web/static && \
    chown -R 755 /data/web/media && \
    chown -R +x /scripts

ENV PATH="/scripts:/venv/bin:$PATH"

USER  duser

CMD [ "commands.sh" ]

