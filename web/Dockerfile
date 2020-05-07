# Build image
FROM python:3.8.2-alpine as build

# Set workdir for build
WORKDIR /usr/src/app

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk add --update-cache postgresql-dev build-base

# Upgrade PIP
RUN pip install --upgrade pip

# Build wheel for dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# Final image
FROM python:3.8.2-alpine

# Create app user and group
RUN adduser --disabled-password app app

# Create directories
RUN mkdir /home/app/web
WORKDIR /home/app/web

# Install dependencies
COPY --from=build /usr/src/app/wheels /wheels
COPY --from=build /usr/src/app/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache /wheels/*

# Copy application
COPY --chown=app:app . /home/app/web

USER app

EXPOSE 5000

ENTRYPOINT ["/home/app/web/entrypoint.sh"]
