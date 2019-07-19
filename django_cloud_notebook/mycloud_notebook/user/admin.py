from django.contrib import admin

# Register your models here.

# 当前文件为: user/admin.py
from . import models

admin.site.register(models.User)

