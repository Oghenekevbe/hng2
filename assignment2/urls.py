from django.urls import path
from .views import *


urlpatterns = [
    path("api", api.as_view(), name="api"),
    path("api/<int:pk>", api.as_view(), name="api"),
    path("api/<str:name>", api.as_view(), name="api"),
]