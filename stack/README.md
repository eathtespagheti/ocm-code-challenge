# Docker stack

## Get up the containers

Just run `docker-compose up -d`, there's a file named [bootstrap.sh](../src/federica_crawler/bootstrap.sh) that manage the first startup

## Env variables

Some variables usage explained:

* `DJANGO_SETTINGS_MODULE`: tells django where project settings module it's located, required in order to use `django-admin`
* `ADMIN_NAME`: default admin name
* `ADMIN_EMAIL`: default admin email
* `ADMIN_PASSWORD`: default admin password, should be avoided and used [docker secrets](#secrets) instead

## Secrets

There's a docker secret for the default admin password and it's named `django-admin-password`
