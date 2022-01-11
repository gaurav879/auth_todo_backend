from django.urls import path

from .views import *

urlpatterns = [
    path("", Home.as_view()),
    # path("data", Data.as_view()),
]
