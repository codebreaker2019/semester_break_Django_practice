from django import forms


class UserForm(forms.Form):
    boolean_field = forms.BooleanField()

