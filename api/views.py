from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def getData(request):
    data = {
        "name": "Anirudh",
        "age": 20,
        "city": "Bangalore"
    }
    return Response(data)