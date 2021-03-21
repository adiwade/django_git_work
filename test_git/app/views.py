from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def show_message(request):
    return HttpResponse("from view.....")
def show_sub(request):
    return HttpResponse("from sub view....")
