from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

choice=(

    ('1','anolog'),

    ('1','logic'),

    ('2','power'),

    ('3','storage'),

    ('4','other')

)
# Create your models here.
class datasheet(models.Model):
    file=models.FileField(blank=True,upload_to='file/',default=None)
    value=models.CharField(max_length=30,unique=True)
    des=models.TextField()
    field=models.CharField(choices=choice,max_length=30)
admin.site.register(datasheet)
