
from django.contrib import admin
from django.urls import path
from .views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage)
]
