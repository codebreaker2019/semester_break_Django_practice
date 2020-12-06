from django import forms


class user_form(forms.Form):
    user_name = forms.CharField(label="Name",widget=forms.TextInput(attrs={'placeholder':'Enter your name'}))
    user_email = forms.EmailField()
    user_birthdate = forms.DateField(label='BirthDate',widget=forms.TextInput(attrs={'type':'date'}))


