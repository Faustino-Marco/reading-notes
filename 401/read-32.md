# Permissions & Postgresql

## Reading
[DRF Permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- Permissions
    - Authentication/ID alone not enough
        - must have authorization
    - permissions, auth, throttling determine request grant or deny
- How Permissions are determined
    - exceptions 
        - perm denied
        - not auth
- Set permission policy
    - default perm classes in setings
- API Reference 
    - isauth
    - isadminuser
    - is staff
    - is auth or read only
    - model permissions
- Object permissions
    - only applied to .queryset property views (like models)
[Review SQL Prework](https://codefellows.github.io/common_curriculum/prep_work/SQL)
## Bookmark & Review
[Classy Django REST](http://www.cdrf.co/)
[DRF Generic Views](https://www.django-rest-framework.org/api-guide/generic-views/)
## TIWKMA
- When would it be prudent to allow users access to manipulate an api?