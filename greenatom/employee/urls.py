from django.urls import path

from .views import *

urlpatterns = [
    path('create_j_d', create_j_d, name="create_j_d"),
    path('<int:a>.doc', download),
    path('<path:a>', page_405),
    path('', page_403),
]

