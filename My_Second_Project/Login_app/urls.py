from django.urls import path
from django.conf.urls import url
from Login_app import views

app_name = 'Login_app'

urlpatterns = [
    path('', views.index, name="index")
]