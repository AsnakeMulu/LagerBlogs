# Django REST Blog API

A simple blog backend built using **Django REST Framework**. This project provides a RESTful API to manage blog posts — including creating, viewing, editing, and deleting posts.

## Features

- Create new blog posts
- View a list of all posts
- View details of a single post
- Update existing posts
- Delete posts
- RESTful API with browsable interface

## Tech Stack

- Python
- Django REST Framework

## Installation

1. **Clone the repo**

```bash
git clone https://github.com/AsnakeMulu/LagerBlogs.git
cd LagerBlogs
```

2. **Create a virtual environment**

```bash
python -m venv env
env/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run the server**

```bash
python manage.py runserver
```
