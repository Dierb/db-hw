from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewCreateAPIview.as_view()),
    path('reviews/<int:id>/', views.ReviewUpdateDeleteAPIView.as_view()),
    path('movie/', views.MovieCreateAPIView.as_view()),
    path('movie/<int:id>/', views.MovieUpdateDeleteAPIView.as_view()),
    path('directors/', views.DierectorCreateAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorUpdateDeleteAPIView.as_view()),
    path('register/', views.RegisterAPIVews.as_view())
]