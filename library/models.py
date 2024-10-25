from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    slug = models.SlugField(blank=True,null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    def __str__(self):
        return self.name