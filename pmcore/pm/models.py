
from distutils.command.upload import upload
from django.db import models
from django.forms import IntegerField


# Create your models here.
class Blog(models.Model):
  title=models.CharField(max_length=200, null=True, blank=True)
  slug = models.SlugField(max_length = 50)
  description=models.TextField(max_length=200, null=True, blank=True)
  date=models.TextField(max_length=200, null=True, blank=True  )
  image=models.ImageField(upload_to='images/')
  
  def __str__(self):
      return self.title
     

class Explore(models.Model):
    
  title = models.CharField(max_length=120,blank=True,null=True)
  descrption=models.TextField(max_length=200, blank=True, null=True)
  image=models.ImageField(upload_to='images/', null=True, blank=True)
  linkto=models.CharField(max_length=200,blank=True, null=True)
    
  def __str__(self):
      return self.title
  
class Admission(models.Model):
    
 work_hours=models.IntegerField()
 number_students=models.IntegerField()
 number_staff=models.IntegerField()
 number_allumn=models.IntegerField()
 

 def __str__(self):
     
     return self.work_hours