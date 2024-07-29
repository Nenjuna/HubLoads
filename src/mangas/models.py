from django.db import models

class Manga(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField()
    rank = models.IntegerField()
    views = models.IntegerField()
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release = models.DateField()
    status = models.CharField(max_length=100)
    cover = models.CharField(max_length=200)
    release = models.DateField()
    
    # def __str__(self):
    #     return self.title