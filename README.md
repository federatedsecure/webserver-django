![CodeQL](https://github.com/federatedsecure/webserver-django/workflows/CodeQL/badge.svg)
![Pylint](https://raw.githubusercontent.com/federatedsecure/webserver-django/main/.github/badges/pylint.svg)

# installing prerequisites

```
pip install django
pip install federatedsecure-server
```

# running the server

```
git clone https://github.com/federatedsecure/webserver-django
cd webserver-django/src
python manage.py runserver <url>:<port>
```