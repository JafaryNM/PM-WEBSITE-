from cgitb import text
from distutils.command.upload import upload
from django.db import models
from django.forms import Textarea
from numpy import blackman

# Create your models here.
class Blog(models.Model):
  title=models.CharField(max_length=200, null=True, blank=True)
  slug = models.SlugField(max_length = 50)
  description=models.TextField(max_length=200, null=True, blank=True)
  date=models.TextField(max_length=200, null=True, blank=True  )
  image=models.ImageField(upload_to='images/')
  
  class  Meta:
        
    def __str__(self):
        return self.title
    
