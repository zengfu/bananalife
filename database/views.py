from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from .models import datasheet
# Create your views here.
def db_index(request,page):
    db_list = datasheet.objects.order_by()
    length = len(db_list)
    pages = length / 20
    page = int(page)
    db_list = db_list[(page - 1) * 20:page * 20]
    return render(request, 'database.html', {'db': db_list, 'pages': range(pages + 1), 'id': page})
def db_test(request):
    for i in range(30):
        a=datasheet.objects.create(file='test',value=i,des='test',field='2')
        a.save()
    return