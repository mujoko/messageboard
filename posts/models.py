from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=200,default='SOME STRING, Title')
    author = models.CharField(max_length=100,default='SOME STRING, Author')

    def __str__(self):  # new
        return self.text[:50]
