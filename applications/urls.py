from django.urls import path
from .views import  RegisterUserAPIView, LoginView
urlpatterns= [
    #path("get-details",UserDetailAPI.as_view()),
    path('register/',RegisterUserAPIView.as_view()),
    path('login/',LoginView.as_view()),
]