from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="director_name")

    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review")

    def __str__(self) -> str:
        return self.text