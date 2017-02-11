#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from .models import BlogsPost
import mistune
import json


# Create your views here.


def blog(request,page):
    markdown=mistune.Markdown()
    blog_list = BlogsPost.objects.order_by('-timestamp')
    length=len(blog_list)
    pages=length/6
    page = int(page)
    blog_list=blog_list[(page-1)*6:page*6]
    for num,i in enumerate(blog_list):
        blog_list[num].body=json.dumps(markdown(i.body))
    return render(request,'blog.html',{'posts':blog_list,'pages':range(pages+1),'id':page})
def post(request,num):
    markdown = mistune.Markdown()
    article=BlogsPost.objects.filter(id=num)
    if article:
        a=article[0].body
        article[0].body=markdown(a)
    else:
        article=[None]
    return render(request,'page.html',{'post':article[0]})


