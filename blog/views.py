#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from .models import BlogsPost
import mistune
# Create your views here.


def blog(request,page):
    markdown=mistune.Markdown()
    blog_list = BlogsPost.objects.order_by('-timestamp')
    length=len(blog_list)
    pages=length/6
    page = int(page)
    blog_list=blog_list[(page-1)*6:page*6]
    for num,i in enumerate(blog_list):
        blog_list[num].body=markdown(i.body)
    return render(request,'blog.html',{'posts':blog_list,'pages':range(pages+1),'id':page})
