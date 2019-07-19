from django.contrib import admin

# Register your models here.
#user/admin.py
from . import models

admin.site.register(models.User)