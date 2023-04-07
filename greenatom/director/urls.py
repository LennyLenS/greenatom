from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('login', login, name="login"),
    path('registration', registration, name="registration"),
    path('storage', storage, name="storage"),
    path('<path:a>', page_405),
    path('', page_403),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)