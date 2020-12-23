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
    new_form = forms.UserForm()
    #form submit holo kina dekhar code
    diction = {'key': 'i am a form  creating by django', 'key_form': new_form}
    if request.method == 'POST':
        new_form = forms.UserForm(request.POST)

        if new_form.is_valid():
            diction.update({'boolean_field':new_form.cleaned_data['boolean_field']})

            diction.update({'form_submit':"Yes"})



    return render(request,'First_app/form.html',context=diction)