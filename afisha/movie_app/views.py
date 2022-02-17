from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirecrotorSerializers, MovieSerializers, ReviewSerializers
from movie_app.models import Director, Movie, Review

@api_view(['get'])
def director_list_view(request):
    directors = Director.objects.all()
    data = DirecrotorSerializers(directors, many=True).data
    return Response(data=data)

@api_view(['get'])
def director_detail_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=404, data={'massage':'director not found'})
    data = DirecrotorSerializers(directors).data
    return Response(data=data)




@api_view(['get'])
def movies_list_view(request):
    movies = Movie.objects.all()
    data = MovieSerializers(movies, many=True).data
    return Response(data=data)

@api_view(['get'])
def movies_detail_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=404, data={'massage':'movie not found'})
    data = MovieSerializers(movies).data
    return Response(data=data)




@api_view(['get'])
def reviews_list_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializers(reviews, many=True).data
    return Response(data=data)

@api_view(['get'])
def reviews_detail_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=404, data={'massage':'review not found'})
    data = ReviewSerializers(reviews).data
    return Response(data=data)