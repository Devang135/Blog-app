from ast import Delete
import imp
from msilib.schema import PublishComponent
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    title = models.models.CharField( max_length=50)
    slug= models.SlugField(maxlength=250,unique_for_date='publish')
    author= models.ForeignKey(User_on_delete=models.CASCADE,related_name='blog_posts')
    body = models.models.TextField()
    publish =models.DateTimeField