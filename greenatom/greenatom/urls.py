

from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('director/', include('director.urls')),
    path('<path:a>', page_405),
    path('', page_404),
]

