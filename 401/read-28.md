# Django CRUD and Forms

## Reading
[Django Forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
- Form refresher*
    - group of one or more fields/widgets on a web page
    - can be used to collect info from users for submission to a server
    - flexible mechanism for collecting user input
        - many different widgets for entering different types of data
        - relatively secure way of sharing data with server
            - allow sending data in POST requests with cross-site request forgery protection
```Python
<form action="/team_name_url/" method="post">
    <label for="team_name">Enter name: </label>
    <input id="team_name" type="text" name="name_field" value="Default name for team.">
    <input type="submit" value="OK">
</form>
```
vs.
```Python
from django import forms

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
```
<hr>


Whole file:
```Python
import datetime

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data
```


## Bookmark and Review
[Django Templates](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page)

[Django Views](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)

## Things I'd like to know more about
- I'm curious about how the cross-site request forgery protection works, on the defensive and offensive side of that type of hacking.