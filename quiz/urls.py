#base urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from quiz_app.views import *

app_name = 'quiz_app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz_app.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
