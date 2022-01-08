from django.urls import path

from .views import *

urlpatterns = [
    path("signup", Signup.as_view()),
    path("", Login.as_view()),
]
