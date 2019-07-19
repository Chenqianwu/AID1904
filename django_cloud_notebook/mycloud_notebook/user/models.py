from django.db import models

# Create your models here.


# file: /user/models.py

class User(models.Model):
    name = models.CharField('姓名', max_length=50)
    password = models.CharField('密码', max_length=50)
    def __str__(self):
        return "用户:" + self.name

