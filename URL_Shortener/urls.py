from django.urls import path
from .views import home, create_short_URL, redirect

urlpatterns = [
    path('', home, name = 'home'),
    path('create_short_URL/', create_short_URL, name = 'create'),
    path('<str:url>', redirect, name = 'redirect')
]