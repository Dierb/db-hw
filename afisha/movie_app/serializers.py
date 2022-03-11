# from django.db.models import fields
from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError

class DirecrotorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name '.split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars author'.split()

class MovieSerializers(serializers.ModelSerializer):
    director = DirecrotorSerializers()

    class Meta:
        model = Movie
        fields = 'title description director '.split()

class MovieReviewsSerializers(serializers.ModelSerializer):
    review = ReviewSerializers(many=True)

    class Meta:
        model = Movie
        fields = 'title review raiting'.split()

class MovieCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.FloatField()
    director_id = serializers.IntegerField()

    def validate(self, attrs):
        id = attrs['director_id']
        try:
            Director.objects.get(id=id)
        except Director.DoesNotExist:
            raise ValidationError(f" director with id={id} not found")
        return attrs



class DirectorCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField()


class ReviewCreateUpdateSerializer(serializers.Serializer):
    stars = serializers.IntegerField()
    text = serializers.CharField()
    movie_id = serializers.IntegerField()

    def validate(self, attrs):
            id = attrs['movie_id']
            try:
                Movie.objects.get(id=id)
            except Movie.DoesNotExist:
                raise ValidationError(f" movie with id={id} not found")
            return attrs
   


