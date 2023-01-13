from django.urls import path
from movie_app.views import (ReviewListCreateAPIView, DirectorListCreateAPIView, DirectorItemUpdateDeleteAPIView,
                             ReviewItemUpdateDeleteAPIView, MovieItemUpdateDeleteAPIView, MovieListCreateAPIView)

urlpatterns = [
    path("directors/", DirectorListCreateAPIView.as_view()),
    path('directors/<int:id>/', DirectorItemUpdateDeleteAPIView.as_view()),
    path('movies/', MovieListCreateAPIView.as_view()),
    path('movies/<int:id>/', MovieItemUpdateDeleteAPIView.as_view()),
    path('reviews/', ReviewListCreateAPIView.as_view()),
    path('reviews/<int:id>/', ReviewItemUpdateDeleteAPIView.as_view())

]
