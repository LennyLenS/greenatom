from django.urls import path

from .views import *

urlpatterns = [
    path('create_j_d', create_j_d, name="create_j_d"),
    path('<path:a>', page_404),
    path('', page_404),
]

