# vi-django
A starter project template for Django
## Project initialization
Run the following commands to install the dependencies:
```bash
```bash
cd theme/static_src 
npm install
```

Run   to build the docker image and run the container.
```bash
docker-compose up -d --build
```
Run the following command to migrate the database:
```bash
docker-compose exec web python manage.py migrate --noinput
```



Run the following command to create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

Run the following command to collect the static files:
```bash
docker-compose exec web python manage.py collectstatic --no-input --clear
```
