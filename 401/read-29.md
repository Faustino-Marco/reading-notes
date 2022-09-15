# Django Custom User

## Reading
[Django Custom User Model](https://learndjango.com/tutorials/django-custom-user-model)
Best Practices: Custom User Model
- Setup
    - Create new project
    - AbstractUser vs AbstractBaseUser
        - both can be subclassed to extend existing fn()
        - A*B*U is MUCH MORE WORK
    - AbstractUser it is!
- Custom User model
    - update project settings
        - add accounts app
        - use AUTH_USER_MODEL config
            - tells django to use our model in place of the built-in user model
            - call ours CustomUser
        - add to installed apps in list
        - also add `AUTH_USER_MODEL = "accounts.CustomUser"` below `INSTALLED_APPS`
    - create new CustomUser model
    - create new UserCreation and UserChanageForm
    - update the admin


[DjangoX](https://github.com/wsvincent/djangox)
- Sick name LOL
- This is a cool Django starter project repo
- I'm curious, but unsure what to do with this resource, or even how to use it exactly.

## Videos
[Creating a Custom User Model](https://www.youtube.com/watch?v=eCeRC7E8Z7Y&t=59s)


[Abstract User, User Profile and Signals in Django](https://www.youtube.com/watch?v=EudKs1HPUfE)
- add user model
- `from django.contrib.auth.models import AbstractUser`
- `class User(AbstractUser):`
    - `quota...`
- settings.AUTH_USER_MODEL
    - end of settings file add:
        - `AUTH_USER_MODEL = 'app.USER'`
- migrate
- app
    - models
        - add user model like above ^
- migrate
    - might throw error
    - need 1:1 relationship between quota (content from user class in user model) and User email/usrnm/pswd
    - need to create a post_save signal
    - load signal into the APP
***To be honest this video lost me right about here, I'm moving on to the other video since we get to choose***


## Bookmark and Review
[Substituting a custom User model](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#auth-custom-user)


# Things I want to learn more about
- The Youtuber in the Abstract User video used an extention called graphmodel to look at the connections between all their models visually, I want to find and use it for myself!