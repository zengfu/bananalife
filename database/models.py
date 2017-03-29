from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

choice=(

    ('analog','analog'),

    ('logic','logic'),

    ('power','power'),

    ('storage','storage'),

    ('other','other')

)
# Create your models here.
class datasheet(models.Model):
    file=models.FileField(blank=True,upload_to='file/',default=None)
    value=models.CharField(max_length=30,unique=True)
    des=models.TextField()
    field=models.CharField(choices=choice,max_length=30)
admin.site.register(datasheet)
