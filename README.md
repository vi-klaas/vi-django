# vi-django

A starter project template for Django

## Project initialization

Run the following commands to install the dependencies:

```bash
cp .env.example .env
```

```bash
cd theme/static_src 
npm install
cd ../..
```

Run to build the docker image and run the container.

```bash
docker compose up -d --build
```

Run the following command to migrate the database:

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate --noinput
```

Run the following command to create a superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

Run the following command to collect the static files:

```bash
docker-compose exec web python manage.py collectstatic --no-input --clear
```

Add this as a command to the CI/CD pipeline, e.g. in github actions yaml file:

```
- name: Collect static files
    run: |
      docker-compose exec web python manage.py collectstatic --no-input --clear
```

### Celery
Change the appname in the celery.py file to the name of your app.
```
app = Celery("vidjango")
```
### Caddy

Caddy is used as a reverse proxy to serve the Django app. It is configured to use HTTPS and HTTP/2. It also redirects
all HTTP requests to HTTPS. The configuration file is located at `caddy/Caddyfile`. You can change the domain name and
email address in the file. You can also add more sites to the file. For more information, see
the [Caddy documentation](https://caddyserver.com/docs/caddyfile).
In order to see the Django Debug Toolbar with Caddy, add its IP to the IPS.
To find out the network name, run the following command:

```bash
docker network ls
```

Then, run the following command to inspect the network, e.g.:

```bash
docker network inspect red_companion_default
```

Add the IP address of the Django container to the IPS in the Caddyfile, e.g.:

```python
INTERNAL_IPS = [
    "127.0.0.1",
]

if DEBUG:
    import socket  # only if you haven't already imported this

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
        "127.0.0.1",
        "10.0.2.2",
        "172.20.0.9", # caddy: adapt to the IP of caddy
    ] 
```

#### Self-signed certificate for caddy

When opening the site in Chrome, you will get a warning that the site is not secure. To fix this, you can add a
self-signed certificate to your keychain. This will make the browser trust the certificate and not show the warning.

* First, export the self-signed certificate. You have to access your site via HTTPS, then inspect the site. Click on the
  lock icon beside the URL, then click on "Certificate". In the Certificate viewer that opens, navigate to the "Details"
  tab and then click on "Export". You can export the certificate in a format like .pem or .der.
* Then, press cmd + , on your keyboard to open the Chrome settings. You could also manually navigate to it by clicking
  on the three vertical dots on the top-right -> "Settings".
  Scroll down and select "Show advanced settings..."
* Under the "Privacy and security" section, select "Manage certificates".
* It will open your keychain on Mac. Click on the + button to add a new certificate.
* In the add certificates prompt, navigate to the location where you exported the certificate and select it.
* Then, it will show in the list of certificates.
* After adding, double-click the item, expand the "Trust" setting and configure "When using this certificate:" to "
  Always Trust".
