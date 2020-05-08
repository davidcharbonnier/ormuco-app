# ormuco-app

This is a Python 3.8 application created with Flask & SQLAlchemy that provides a simple form saved in a PostgreSQL 12.2 database.
This python application follows PEP8 codestyle conventions.

## Prerequisites

In order to deploy this application, you need to have the following system packages installed:

- python3
- python-pip
- virtualenv

## Launch application

### Install dependencies

To be able to launch application stack, you need to install dependencies:

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

For next part, we assume that this virtualenv has been created and is still activated.

### Write cnfiguration

Before starting our stack, we need to write 2 configuration files (database and application).

**.env.db** wich contains PostgreSQL configuration to create user and database:

```bash
POSTGRES_USER=<user>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<database>
```

**.env.prod** which contains Flask application settings:

```bash
FLASK_APP=ormuco/__init__.py
FLASK_ENV=production
SECRET_KEY=<secret_key>
DB_HOST=db
DB_PORT=5432
DB_NAME=<database>
DB_USERNAME=<user>
DB_PASSWORD=<password>
```

Data already put in this example is data that should not be updated except if application or docker-compose definition have been modified.

**docker-compose.yml** file also contains settings in labels of the **web** service:

```yaml
# Enable Traefik proxy to expose Ormuco test
- "traefik.enable=true"
- "traefik.http.routers.ormuco.rule=Host(`ormuco.davidcharbonnier.fr`)"
- "traefik.http.routers.ormuco.entrypoints=websecure"
- "traefik.http.routers.ormuco.tls.certresolver=letsencrypt"
```

The `Host()` field is used to issue an SSL certificate from Letsencrypt CA and also redirect trafic from Traefik reverse proxy to our application and should be updated with a real domain name resolving to server hosting this stack.

### Launch stack

To launch stack, you just need to issue this command:

```bash
docker-compose up -d --build
```

On fresh install, you should initialize database with this command:

```bash
docker-compose exec web python manage.py init_db
```

Application should now be accessible at https://url_defined_in_labels_of_compose_file/

## Not yet implemented

Here is list of improvement that could be implemented:

- Use HTTP scheme correctly in `url_for` calls to avoid being redirected from HTTPS to HTTP after submitting a form when application is hosted behind a reverse proxy that handles TLS termination
- Fully implement MVC model (separate routing and control)
- Implement metrics collection with Prometheus client library
- Collect traces with a tracing client library (Zipkin or Jaeger)
