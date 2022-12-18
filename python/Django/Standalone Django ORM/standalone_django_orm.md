# Standalone Django ORM

The thing a love the most of Django is without a doubt its ORM. And sometimes, for really small projects that needs some advanced database queries, I don't wan't to use SQL and also don't wan't to create a full Django project just to enjoy its ORM. 

So, this is a guide on how to use the ORM with the minimal Django configuration possible.

First install Django:

```bash
$ pip install Django
```

Create a packeage to act as a Django app and that will hold the models code:

```bash
$ mkdir db && cd db
$ touch __init__.py
```

In the project base directory create a `manage.py` where we are gonna place the Django configuration and it will also run de manage CLI commands.

```python
from django.core.management import execute_from_command_line
from django.conf import settings
from pathlib import Path
import django
import sys


def start_django():
    try:
        print("[INFO] Starting django db app...")
        if settings.configured:
            return
        BASE_DIR = Path(__file__).resolve().parent
        print(BASE_DIR)
        settings.configure(
            INSTALLED_APPS=[
                "db",
            ],
            DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
            DATABASES={
                "default": {
                    "ENGINE": "django.db.backends.sqlite3",
                    "NAME": Path.joinpath(BASE_DIR, "project_db.sqlite3"),
                }
            },
        )
        django.setup()
    except Exception as e:
        print(f"[ERROR] >>> Django failed at starting:", e)


if __name__ == "__main__":
    start_django()
    execute_from_command_line(sys.argv)
```


Now in the `db` app create a file to place some models and to call the `start_django()` function:

```python
from django.db import models
from manage import start_django


start_django()


class ChatMessage(models.Model):
    message = models.CharField(blank=False, null=False, max_length=1000)
    send_datetime = models.DateTimeField(auto_now_add=True)
    viewed = models.BooleanField(default=False)
```

This way anywhere you import a model, the `start_django()` function will check if the Django is already setup or initialized. 

After create the models you can make and apply the migrations:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

The project structure should look like this:

```
|
|-- db
|   |-- __init__.py
|   |-- models.py
|
|-- manage.py
```

Now you can use the class models like in a normal Django project.

```python
from db.models import ChatMessage

for cm in ChatMessage.objects.all():
    print(cm)
```
