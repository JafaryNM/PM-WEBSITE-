
from ast import Add
from tracemalloc import Statistic
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Blog)
admin.site.register(Explore)
admin.site.register(Admission)



