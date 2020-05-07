#!/bin/sh

# Wait for PostgreSQL to be up and running
echo "Waiting for PostgreSQL to be ready..."
sleep 3 # We need to wait for temporary PostgreSQL server to initialize before final one starts
while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.5
done
echo "PostgreSQL ready"

# Initialize database when in development environment
if [ "$FLASK_ENV" = "development" ]
then
    echo "Initializing development database..."
    python manage.py init_db
    echo "Database initialized"
fi

exec "$@"
