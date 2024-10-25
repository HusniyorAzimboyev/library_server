from django.db import models

class user(models.Model):
    name = models.CharField(max_length=150)
    password = models.SmallIntegerField()
    def __str__(self):
        return self.name