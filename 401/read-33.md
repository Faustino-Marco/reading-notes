# Authentication & Production Server

## Reading
[JSON Web Tokens](https://jwt.io/introduction/)
- JWT pronounced (jot?)
- securely transmitting info between parties as JSON object
    - digitally signed
        - secret
            - HMAC algo
        - public/private key
            - RSA or ECDSA
        - (can be encrypted, not covered here)
- Use for auth, info exchange

[DRF JWT Authentication](https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html)
- should be in all requests
- acquired by exchanging usrnm/pswd for access token & refresh token
- header
- payload
- signature
[Django Runserver Is Not Your Production Server](https://build.vsupalov.com/django-runserver-in-production/)
- django runserver has not gone throgh security audits or performance tests
- Njinx instead
- Gunicorn WSGI server

## Videos
[JWT with DRF](https://www.youtube.com/watch?v=Fhcn2qx-4VQ)

## Bookmark & Review
[Gunicorn](https://gunicorn.org/)
[Django Migrations Primer](https://realpython.com/django-migrations-a-primer/)

## TIWKMA