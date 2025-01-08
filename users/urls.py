from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin_add/', admin.site.urls),
    ]