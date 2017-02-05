#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from .models import BlogsPost
import mistune
# Create your views here.


def blog(request):
    markdown=mistune.Markdown()
    blog_list = BlogsPost.objects.all()
    for num,i in enumerate(blog_list):
        print len(i.body)
        #blog_list[num].body=i.body.replace('\n','</br>')
        #blog_list[num].body = i.body.replace(' ', '&nbsp')
        blog_list[num].body=markdown(i.body)
    return render(request,'blog.html',{'posts':blog_list})
