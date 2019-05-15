from django.db import models

# Create your models here.

class user_plan(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    choosen_plan = models.IntegerField()

class social_post(models.Model):
    username = models.CharField(max_length=100)
    post = models.TextField()
