# Federica crawler django app

Django app to manage data scraped from [Federica](https://www.federica.eu)

## Models

Data it's organized in 4 models, all from the [`apps.courses.models`](apps/courses/models.py) module

To check how the data it's obtained and stored check scrapy project's [README](apps/crawler/README.md#pipelines)

### Course

Main model representing a COOM, fields are:

* `title`: CharField
* `url`: URL to Course info webpage
* `area`: FK to [Area](#area) model
* `status`: FK to [Status](#status) model
* `teacher`: FK to [Teachet](#teacher) model (should be a ManyToMany field, but I didn't had enough time)
* `short_description`: Short description for the [all moocs](https://www.federica.eu/en/all-moocs/) page
* `long_description`: Full description from the info webpage

### Status

Represent a Course status, known possible values from the scraped data are `NOW OPEN` and `TO BE ANNOUNCED`

Status value it's stored in the only availabe field, `value`

### Area

Represent a Course area, known possible values from the scraped data are `Università`, `Orientamento` and `Federica Pro`

Area value it's stored in the only availabe field, `value`

### Teacher

Represent a Course teacher, since some teachers have multiple courses seems reasonable to create a separate model and take advantage of references

Teachers names it's stored in the only availabe field, `name`

## Templates and views

### Templates

All templates are just a few lines of HTML and use bootstrap 5

### Views 

All Views are in the [`apps.courses.views`](apps/courses/views.py) module:

* `IndexView`: Manage the main Course index
* `DetailView`: Manage details for Course instances
* `ButtonActions`: Called from `buttons`, manage all the actions available form the form

## Tests

There are some tests for [`apps.courses.models`](apps/courses/models.py) in [`apps.courses.tests`](apps/courses/tests.py) and some pipelines tests in [`federica_crawler.tests`](federica_crawler/tests.py)

All tests can be launched with

```sh
django-admin test
```

## How to demo the project

### First run

First run will require you three things to setup database and super user

```sh
django-admin migrate
django-admin createsuperuser
django-admin runserver
```

`django-admin migrate` will create tables in the database according to the django models in the project
`django-admin createsuperuser` it's for creating the superuser (will require you to type some info)
`django-admin runserver localhost:8000` : runs the server, now you can browse your project from [here](http://localhost:8000)

### Next runs

Now you can simply run the server with `django-admin runserver localhost:8000` (or any other ip:port combination)