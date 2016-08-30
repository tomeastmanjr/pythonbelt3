from __future__ import unicode_literals
from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey("loginreg.User", related_name = "creator")
    adders = models.ManyToManyField("loginreg.User", related_name = "adders")
