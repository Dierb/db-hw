from django.contrib.auth import authenticate
from django.db import reset_queries
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirecrotorSerializers, MovieSerializers, ReviewSerializers, MovieReviewsSerializers,\
MovieCreateUpdateSerializer, DirectorCreateUpdateSerializer, ReviewCreateUpdateSerializer
from movie_app.models import Director, Movie, Review
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@api_view(['GET', 'POST'])
def director_list_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirecrotorSerializers(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = DirectorCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        print(request.data)
        name = request.data.get('name')
        director =Director.objects.create(name=name)
        return Response(data=DirecrotorSerializers(director).data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=404, data={'massage':'director not found'})
    if request.method == 'GET':
        data = DirecrotorSerializers(directors).data
        return Response(data=data)
    elif request.method == 'DELETE':
        directors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        directors.name = request.data.get('name')
        directors.save()
        return Response(data=DirecrotorSerializers(directors).data)




@api_view(['GET','POST'])
def movies_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializers(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = MovieCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data=MovieSerializers(movie).data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=404, data={'massage':'movie not found'})
    if request.method == 'GET':
        data = MovieSerializers(movies).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movies.title = request.data.get('title')
        movies.description = request.data.get('description')
        movies.duration = request.data.get('duration')
        movies.director_id = request.data.get('director_id')
        movies.save()
        return Response(data=MovieSerializers(movies).data)





@api_view(["GET",'POST'])
def reviews_list_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializers(reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ReviewCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        print(request.data)
        stars = request.data.get('stars')
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        review = Review.objects.create(stars=stars, text=text, movie_id=movie_id)
        return Response(data=ReviewSerializers(review).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=404, data={'massage':'review not found'})
    if request.method == 'GET':
        data = ReviewSerializers(reviews).data
        return Response(data=data) 
    elif request.method == 'DELETE':
        request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        reviews.stars = request.data.get('stars')
        reviews.text = request.data.get('text')
        reviews.movie_id = request.data.get('movie_id')
        reviews.save()
        return Response(data=ReviewSerializers(reviews).data)




@api_view(['get'])
def MoviesRewiews(request):
    reviews = Movie.objects.all()
    data = MovieReviewsSerializers(reviews, many=True).data
    return Response(data=data)


@api_view(['POST'])
def autorization(request):
    if request.method == "POST":
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'key': token.key})
        return Response(data={'error':'user not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def registration(request):
    if request.method == "POST":
        username = request.data.get('username')
        password = request.data.get('password')
        User.objects.create_user(username=username, password=password)
        return Response(data={'massage':"user created"}, status=status.HTTP_201_CREATED)

