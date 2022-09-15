# Django REST Framework & Docker

## Reading
[Beginner's Guide to Docker](https://wsvincent.com/beginners-guide-to-docker/)
- Linux Containers
    - type of virtualization
        - vm
        - sharing copies of a computer system
    - downside
        - size / speed
    - "containerization"
        - linux containers specifically growing in popularity
    - VM's are like homes
        - Docker containers are like apartments
    - venv
        - pointing at a system-wide installation within package
- Images
    - codes path to new file
- image builds
```Python
$ docker image build .
Sending build context to Docker daemon  2.048kB
Step 1/1 : FROM python:3.7-alpine
3.7-alpine: Pulling from library/python
c9b1b535fdd9: Pull complete
2cc5ad85d9ab: Pull complete
53a2fca3c2ea: Pull complete
30fce49de8b1: Pull complete
49bcb9571cc7: Pull complete
Digest: sha256:7655eea15dfd981eeb7d243af21e8561e967709caba938d50b136cdb992f3546
Status: Downloaded newer image for python:3.7-alpine
 ---> b2c276538711
Successfully built b2c276538711
```

- image layering
    - each layer is immutable-unchanged-like a git commit
    - performance
        - docker caches steps for subsequent builds
            - changes affect all steps after change
- containers
    - now "Dockerize" a basic django web app


[Django for APIs - Library Website](https://djangoforapis.com/library-website-and-api/)
- Traditional Django
    - this is a site outlining how to build a library app?

## Bookmark & Review
[Beginner's Guide to Docker](https://wsvincent.com/official-django-rest-framework-tutorial-beginners-guide)

## Things I Want to Know More About
- WRRC in context of Docker!