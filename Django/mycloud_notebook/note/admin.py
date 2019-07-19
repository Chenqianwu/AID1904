from django.contrib import admin

# Register your models here.
#note/admin.py
from . import models

admin.site.register(models.Note)