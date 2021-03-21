from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def show_add(request):
    return HttpResponse("from add view.....")
def show_message(request):
    return HttpResponse("from view.....")