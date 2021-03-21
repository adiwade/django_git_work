from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def email_git(request):
    return HttpResponse("from email git....")