from django.db import models

class user(models.Model):
    login_user =  models.AutoField(primary_key=True)
    login_pass = models.CharField(max_length=12)