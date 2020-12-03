from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.
def index(request):
    diction = {'key_1': 'I am coming from views'}
    return render(request, 'First_app/index.html', context=diction)


def contact(request):
    diction = {'key_2': 'I am from views'}
    return render(request, 'First_app/contact.html', context=diction)