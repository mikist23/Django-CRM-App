from django.urls import path
from .views import home, register


urlpatterns = [
    path('', home, name=''),
    path('register/', register, name='register' ),
]
