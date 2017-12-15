# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Series(models.Model):
    Series_Name = models.CharField(max_length=30)
    Author = models.CharField(max_length=40)
    Genre = models.CharField(max_length=25)
    PublicationDate = models.CharField(max_length=8)
    def __str__(self):
        return self.Series_Name + " made by  " + self.Author + " released in " + self.PublicationDate

class Book (models.Model):
    mySerie = models.ForeignKey(Series, on_delete=models.CASCADE)
    Book_Name = models.CharField(max_length=25)
    def __str__(self):
        return  ("%s from the series %s " %(self.Book_Name,str(self.mySerie)))