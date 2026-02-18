from .views import *
from django.urls import path

urlpatterns = [
    path("", getData, name="getdata"),
]