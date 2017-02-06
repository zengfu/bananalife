from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

class imgds(models.Model):
    img = models.ImageField(blank=True, upload_to='img/',default=None)

admin.site.register(BlogsPost,BlogPostAdmin)
admin.site.register(imgds)