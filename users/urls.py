from django.urls import path
from users import views


urlpatterns = [
    path('authorization/', views.AuthorizeAPIView.as_view()),
    path('registration/', views.RegisterAPIView.as_view())
]