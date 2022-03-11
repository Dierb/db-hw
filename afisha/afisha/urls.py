from django.contrib import admin
from django.urls import path, include
from rest_framework import views
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.director_list_view),
    path('api/v1/movies/', views.movies_list_view),
    path('api/v1/reviews/', views.reviews_list_view),
    path('api/v1/directors/<int:id>/', views.director_detail_view),
    path('api/v1/movies/<int:id>/', views.movies_detail_view),
    path('api/v1/reviews/<int:id>/', views.reviews_detail_view),
    path('api/v1/movies/reviews/', views.MoviesRewiews),
    path('api/v1/login/', views.autorization),
    path('api/v1/registration/', views.registration),
    path('api/v1/cbv/', include('cbv.urls'))

]
