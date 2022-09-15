# Django

## Reading
[Getting Started with Django]()
Invented to meet fast-moving newsroom deadlines while still satisfying the tough requirements of experienced web devs.

- Why Django?
    - concept to launch in hours
    - takes care of much of the hassle of web dev
    - "fully loaded"
        - auth
        - admin
        - site maps
        - RSS
        - etc., OOTB
    - secure
        - avoids
            - sql injection
            - cross-site scripting
            - cross-site request forgery
            - clickjacking
    - scalable
        - "shared-nothing" architecture
            - can add hardware at any level
                - db servers
                - caching servers
                - web/app servers
        - clean separation between db layer and app layer
        - ships with simple-yet-powerful cache framework
    - Developed by World Online
        - web dept. of a newspaper in Lawrence, Kansas, USA.
        - now run by an international team of volunteers.
    - licensing
        - 3-clause BSD license
        - open source license granting broad permissions to modify and redistribute Django
        - includes Python's licnse file
            - django includes code from PSL
            - license must include python's license file per Python's terms
- Models
    - Py Class
    - attributes represent database field
    - auto generates database access API
```Python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

- how to use models
    - change settings -> installed apps

- Fields
    - column type (integer, varchar, text)
    - default html widget to use
    - minimal validation reqs
    - options
        - null
        - blank
        - choices
- Urls
    - create a Py mod called URLconf
    - acts as table of contents for app
- Templates
    - disigned to strike balance between power and ease
    - flexibility to augment templates as needed
- Forms
    - handles forms as HTML
    - generate forms from your existing models and use to create and update data
- Authentication
    - full-featured and secure auth system included in django
    - handles user accounts, groups, permissions, and cookie-based user sessions. 
- Admin
    - automatic admin interface
    - reads metadata in your models to provide interface  to manage content
- Internationalization
    - full support for translating text into different languages
    - locale-specific formatting of dates, times, nums, time zones
- Security
    - protects against
        - clickjacking
        - cross-site scripting
        - cross-site requrest forgery
        - SQL injection
        - Remote code execution

[How Django Works Behind the Scenes]()

## Bookmark and Review
[What is Django]()
[First Django App - Pt 1]()
[First Django App - Pt 2]()

