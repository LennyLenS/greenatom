from django.urls import path

from .views import *

urlpatterns = [
    path('create_j_d', create_j_d),
]