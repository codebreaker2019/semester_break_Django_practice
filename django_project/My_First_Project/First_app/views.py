from django.shortcuts import render
#from django.http import HttpResponse
from First_app import forms


# Create your views here.
def index(request):
    diction = {'key_1': 'I am coming from views'}
    return render(request, 'First_app/index.html', context=diction)


def contact(request):
    diction = {'key_2': 'I am from views'}
    return render(request, 'First_app/contact.html', context=diction)


def form(request):
    new_form = forms.user_form()
    diction = {'key':'i am from html page','key_form': new_form}
    if request.method == 'post':
        new_form = forms.user_form(request.post)
        if new_form.is_valid():
            user_name = new_form.cleaned_data['user_name']
            user_birthdate = new_form.cleaned_data['user_birthdate']
            user_email = new_form.cleaned_data['user_email']
            diction.update({'user_name':user_name})
            diction.update({'user_email':user_email})
            diction.update({'user_birthdate':user_birthdate})
            diction.update({'form_submitted': "Yes"})
    return render(request,'First_app/form.html',context=diction)