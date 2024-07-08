from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, Django! this is my first Django project.")
    # return render(request, 'home.html')
    return render(request, 'website/index.html', {'name': 'John'})


def about(request):
    return HttpResponse("This is the about page of my Django project.")


def contact(request):
    return HttpResponse("This is the contact page of my Django project.")


def security(request):
    return HttpResponse("This is the security page of my Django project.")