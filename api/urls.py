from .views import *
from django.urls import path

urlpatterns = [
    path("getdata/", getData, name="getdata"),
]