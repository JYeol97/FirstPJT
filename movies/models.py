from django.db import models

# Create your models here.


# Actor가 환자
class Actor(models.Model):
    name = models.CharField(max_length=100)


# Movie가 의사
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    actors = models.ManyToManyField('Actor', related_name='actors_movies')

class Review(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
