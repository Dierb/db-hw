from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
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

    @property
    def raiting(self):
        reviews = Review.objects.filter(movie=self)
        sum_ = 0
        for i in reviews:
            sum_ += i.stars
        try:
            return sum_/reviews.count()
        except:
            return 0
    

class Review(models.Model):
    stars = models.IntegerField(default=5)
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)

    def __str__(self) -> str:
        return self.text


    