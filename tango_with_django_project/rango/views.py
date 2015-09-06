from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Rango says Hey There World</h1> <p> <a href="http://localhost:8000/rango/about">Visit our About page</a>')
def about(request):
    return HttpResponse('<h1>Rango says About Page</h1> <p> <a href="http://localhost:8000/rango">Visit Home page</a>')

