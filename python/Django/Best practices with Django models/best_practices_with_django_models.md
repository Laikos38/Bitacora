# Best practices with Django models

Recommendations and good practices when implementing Django models. Starting from basic and simple recommendations to advanced ones.

-------------

### 1. Naming models
Use singular nouns for model naming. For example, "Post", "Article".

<br>

### 2. Relational names
Use logical names for relationship fields, for example, in a model where an User represents the author of an Article, use something meaningful like "author" not "user":

```python
class User(models.Model):
    ...

class Article(models.Model):
    author = models.ForeignKey(User, ... )
```
Don't use "_id" suffix for field names in relationships.

<br>

### 3. Naming related_name
Use plural related_name, as these returns querysets (except in OneToOneFields). In majority of cases plural is the way to go.

```python
class User(models.Model):
    ...

class Article(models.Model):
    author = models.ForeignKey(User, related_name="articles")

user = User.objects.get(id=1)
user_articles = user.articles.all() # Queryset
```

<br>

### 4. Just use OneToOneField
Don't use ForeignKey with `unique=True`, just use `OneToOneField`.

<br>

### 5. BooleanField
Don't use `null=True` or `blank=True` in BooleanField, its better if you specify a default value instead. If not use NullBooleanField. 

<br>

### 6. Choices
When using [choices](https://docs.djangoproject.com/en/3.2/ref/models/fields/#choices), variables names for variants should be indicated in uppercase, because are constants. Also, indicate the variantes chronologically before the fields lists. Using choices is a great practice. I also like to use strings for the variants, as I see it more readable.

```python
class Article(models.Model):
    CREATED = 'created'
    IN_REVISION = 'in_revision'
    ACCEPTED = 'accepted'
    DELETED = 'deleted'
    STATUS_CHOICES = [
        (CREATED, 'Created'),
        (IN_REVISION, 'In revision'),
        (ACCEPTED, 'Accepted'),
        (DELETED, 'Deleted')
    ]

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=CREATED
    )
```
If your model has several status flags, its maybe better to use choices.

<br>

### 7. Use specific fields
For example, if you want to save the height of a person, use PositiveIntegerField instead of IntegerField.

<br>

### 8. Never make len(queryset) or if queryset
Do not use len to get queryset’s objects amount. The `count` method can be used for this purpose. Like this: `len(ModelName.objects.all())`, firstly the query for selecting all data from the table will be carried out, then this data will be transformed into a Python object, and the length of this object will be found with the help of len. It is highly recommended not to use this method as count will address to a corresponding SQL function COUNT(). With count, an easier query will be carried out in that database and fewer resources will be required for python code performance.

Similar to this, don't use `if queryset`, use `if queryset.exists()`.

<br>

### 9. Money information storage
For representating money in a model, don't use `FloatField`, use `DecimalField` instead

<br>

### 10. null and blank in string-based fields
Avoid using null on string-based fields such as CharField and TextField. If a string-based field has null=True, that means it has two possible values for “no data”: NULL, and the empty string. In most cases, it’s redundant to have two possible values for “no data;” the Django convention is to use the empty string, not NULL. One exception is when a CharField has both unique=True and blank=True set. In this situation, null=True is required to avoid unique constraint violations when saving multiple objects with blank values.

For both string-based and non-string-based fields, you will also need to set blank=True if you wish to permit empty values in forms, as the null parameter only affects database storage (see blank).

<br>

### 11. Define `__str__` method
In all non abstract models, add methods `__unicode__` (python 2) or `__str__` (python 3). These methods must always return strings.

<br>

### 12. Do not heap all files loaded by user in the same folder
Sometimes even a separate folder for each FileField will not be enough if a large amount of downloaded files is expected. Storing many files in one folder means the file system will search for the needed file more slowly. To avoid such problems, you can do the following:
```python
class MyModel(models.Model):
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
```

<br>

### 13. Use abstract models
If you want to share some logic between models, you can use abstract models.
```python
from django.db import models

class CommonInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
```
But [be careful with related name and related query name](https://docs.djangoproject.com/en/3.2/topics/db/models/#be-careful-with-related-name-and-related-query-name).

<br>

### 14. Use custom Manager and QuerySet
Adding extra Manager methods is the preferred way to add “table-level” functionality to your models.

```python
from django.db import models
from django.db.models.functions import Coalesce

# Custom manager
class PollManager(models.Manager):

    # Custom manager method
    def with_counts(self):
        return self.annotate(
            num_responses=Coalesce(models.Count("response"), 0)
        )

class OpinionPoll(models.Model):
    question = models.CharField(max_length=200)
    objects = PollManager()

class Response(models.Model):
    poll = models.ForeignKey(OpinionPoll, on_delete=models.CASCADE)
    ...
```
With this example, you’d use OpinionPoll.objects.with_counts() to get a QuerySet of OpinionPoll objects with the extra num_responses attribute attached.

A custom Manager method can return anything you want. It doesn’t have to return a QuerySet.

Another thing to note is that Manager methods can access self.model to get the model class to which they’re attached.

While most methods from the standard QuerySet are accessible directly from the Manager, this is only the case for the extra methods defined on a custom QuerySet if you also implement them on the Manager:

```python
from django.db import models
from django.db.models.functions import Coalesce


class PersonQuerySet(models.QuerySet):
    def type_true_false(self):
        return self.filter(type=...)

    def type_multiple_choice(self):
        return self.filter(type=...)


# Custom manager
class PollManager(models.Manager):

    # Custom manager method
    def with_counts(self):
        return self.annotate(
            num_responses=Coalesce(models.Count("response"), 0)
        )
    
    def type_true_false(self):
        return self.get_queryset().type_true_false()

    def type_multiple_choice(self):
        return self.get_queryset().type_multiple_choice()


class OpinionPoll(models.Model):
    question = models.CharField(max_length=200)
    objects = PollManager()

class Response(models.Model):
    poll = models.ForeignKey(OpinionPoll, on_delete=models.CASCADE)
    ...
```

This example allows you to call both authors() and editors() directly from the manager Person.people.

[Creating a manager with queryset methods](https://docs.djangoproject.com/en/3.2/topics/db/managers/#creating-a-manager-with-queryset-methods)

[Custom managers and model inheritance](https://docs.djangoproject.com/en/3.2/topics/db/managers/#custom-managers-and-model-inheritance)

<br>

### 15. Cool modules

#### Django model utils
[Django model utils](https://django-model-utils.readthedocs.io/en/latest/index.html)

#### Django softdelete with cascade implementation

[Django softdelete](https://github.com/scoursen/django-softdelete)