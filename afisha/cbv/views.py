from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from movie_app.models import Review , Movie, Director
from movie_app.serializers import MovieSerializers, ReviewSerializers, DirecrotorSerializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializers

# ====================================================================================

class ReviewCreateAPIview(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    pagination_class = PageNumberPagination

class ReviewUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    lookup_field = 'id'

# ====================================================================================

class MovieCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    pagination_class = PageNumberPagination

class MovieUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    lookup_field = 'id'

# ====================================================================================

class DierectorCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirecrotorSerializers
    pagination_class = PageNumberPagination

class DirectorUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirecrotorSerializers
    lookup_field = 'id'
    
# ====================================================================================

class RegisterAPIVews(APIView):
    serializer_class = UserCreateSerializers

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # username = request.data.get('username')
        # password = request.data.get('password')
        User.objects.create_user(**serializer.validated_data)
        return Response(data={'massage':"user created"}, status=status.HTTP_201_CREATED)
