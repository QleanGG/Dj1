from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def index(req):
    return JsonResponse('hello World!! I\'m using Django!', safe=False)
