# Django Models

## Reading
[Using Models](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)
- Designing LocalLibrary models
    - separate models for every "object" or group of info
        - ex. books, book instances, authors
    - could represent different list selection options
        - like in a dropdown
    - Fields
        - onetoone
        - foreignkey
        - onetomany
    - based on the graphic on the site:
        - each model has elements to define
            - title:String
            - author:Author[1]
            - summary:String
            - ISBN:String
            - genre:Genre[1..*]
            - language:Language[1]
- Model Primer
    - Model definition
        - defined in models.py
    - subclasses of django.db.models.Model
```Python
from django.db import models
from django.urls import reverse

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    # …

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name
```

- Fields
    - represents a column of data that we want to store in one of our database tables
    - each will consist of one of each field value
```Python
my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
```

[Django Admin](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site)
- Register models with admin site
- login
- create some data
- fine-tune presentation of admin site

- Admin is an <em>application<em> in the project
    - uses models to automatically build a site area that you can use to create, view, update, and delete records.
    - easy to test models
    - manage data in production (depends on type of site)
    - really only for actual admins, not rec'd for users
- Register Models
    - `from django.contrib import admin`
    - `from .models import Author, Genre, Book, BookInstance`
    - `admin.site.register(Book)`
    - `admin.site.register(Author)`
    - `admin.site.register(Genre)`
    - `admin.site.register(BookInstance)`
- Create a SuperUser
    - "staff" status enabled, in order view and create records
    - permissions to manage all objects
    - create superuser account that has full access to the site and all needed permissions using `manage.py`

[Beginner's Guide to Django - pt 1](https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html)

## Bookmark and Review
[Beginner's Guide to Django - pt 2](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html)

## Things I'd like to know more about