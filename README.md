# Jijue
- HIV Risk assessment website

# To Start

## Setup

The first thing to do is to clone the repository:

```sh
$ https://github.com/sphinx-austin/flowbite-django-tailwind.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages venv

or py -3 -m venv ven

$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Create the node modules for tailwind and Flowbite

```sh

$ npm start
```

Run the following command to watch for changes and compile the Tailwind CSS code:
```sh

npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
```

Install Flowbite
```sh
npm install flowbite
```




Run the server:

```
(env)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/

ALL SET.
