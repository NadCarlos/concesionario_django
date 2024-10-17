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



## Api
Added API for: Car, Review and User

Examples on how to use it:

**Call:**
```http
GET /api/car_apiview/
```

**Expected Output:**
```
[
  {
    "name": "Cronos",
    "pk": 6,
    "brand": 1,
    "stock": 31,
    "category": {
      "name": "Sedan",
      "pk": 3
    },
    "description": "El mas comprado de la marca",
    "price": "2500000.00"
  },
  {
    "name": "Up",
    "pk": 7,
    "brand": 2,
    "stock": 10,
    "category": {
      "name": "Hatchback",
      "pk": 2
    },
    "description": "el upe",
    "price": "145555.00"
  }
]
```

**Call:**
```http
GET /api/coment_apiview/<valid_car_id>/
```

**Expected Output:**
```
[
  {
    "car": 6,
    "author": 1,
    "text": "review text1",
    "date": "2024-08-05",
    "rating": 5
  },
  {
    "car": 6,
    "author": 2,
    "text": "review text2",
    "date": "2024-08-05",
    "rating": 3
  },
]
```

**Call:**
```http
GET /api/user_apiview/
```

**Expected Output:**
```
[
    {
        "id": 1,
        "username": "user1",
        "first_name": "name1",
        "last_name": "lastname1",
        "email": "email@1.com"
    },
    {
        "id": ,
        "username": "user2",
        "first_name": "name2",
        "last_name": "lastname2",
        "email": "email@2.com"
    },
]
```

**Call:**
```http
GET /api/user_apiview/
```

**Input:**
```
{
    "username": "new_user",
    "first_name": "new_name",
    "last_name": "new_lastname",
    "email": "new_email@email.com"
}
```

**Expected Output:**
```
{
    "id": 3,
    "username": "new_user",
    "first_name": "new_name",
    "last_name": "new_lastname",
    "email": "new_email@email.com"
}
```
