from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def main_page(request):
    return HttpResponse(content="Main Page")


def hello_world(request):
    return HttpResponse(content="Hello World")


def hello_personalized(request, name, lastname):
    return HttpResponse(content=f"Hello {name} {lastname}")

# Kalkulator
#
#
# def addition(request, a, b):
#     return HttpResponse(content=float(a) + float(b))
#
#
# def substraction(request, a, b):
#     return HttpResponse(content=float(a) - float(b))
#
#
# def multiply(request, a, b):
#     return HttpResponse(content=float(a) * float(b))
#
#
# def divide(request, a, b):
#     return HttpResponse(content=float(a) / float(b))
