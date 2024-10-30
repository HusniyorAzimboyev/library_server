from django.db import models

class upper(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    def __str__(self):
        return self.username
class just_log(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    age = models.SmallIntegerField(max_length=3)
    def __str__(self):
        return self.name