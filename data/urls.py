from django.urls import path
from .views import *

urlpatterns = [
    path("fetch_data/", fetch_data, name="fetch_data"),
]
