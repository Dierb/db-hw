from django.db.models import fields
from rest_framework import serializers
from movie_app.models import Director, Movie, Review

class DirecrotorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie'.split()