# Simple Dealership App

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:NadCarlos/concesionario_django.git
$ cd concesionario_django
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd concesionario
```

## Migrations
Run migrations

```sh
(env)$ python manage.py migrate
```

## Superuser
Run migrations

```sh
(env)$ python manage.py createsuperuser
```

Create your admin account and navigate to `http://127.0.0.1:8000/admin/`.

## Data
Add all the data you want and then navigate to `http://127.0.0.1:8000/` to see the interface so you
can start interacting with it

