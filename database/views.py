from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms

# Create your views here.
def db_index(request):
    return render(request,'database.html')