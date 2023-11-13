from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('generator.urls', namespace='main')),
    path('admin/', admin.site.urls),
]