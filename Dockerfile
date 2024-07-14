FROM python:3.10-bookworm
LABEL maintainer='juliana13290@gmail.com'

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install netcat alternative
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy folders into the container
COPY djangoapp /djangoapp
COPY scripts /scripts

# Set working directory
WORKDIR /djangoapp

# Expose port 8000
EXPOSE 8000

# Install dependencies, create user, set permissions
RUN python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /djangoapp/requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    chown -R duser:duser /venv && \
    chmod -R +x /scripts

# Add scripts and venv/bin to $PATH
ENV PATH="/scripts:/venv/bin:$PATH"

# Switch user
USER duser

# Run commands.sh script
CMD [ "commands.sh" ]
