from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/polls/')),  # Home → Polls
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]