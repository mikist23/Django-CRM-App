from django.urls import path
from .views import home, register,login,dashboard,logout


urlpatterns = [
    path('', home, name=''),

    path('register/', register, name='register' ),

    path('login/', login, name='login' ),

    path('logout/', logout, name='logout' ),

    path('dashboard/', dashboard, name='dashboard' ),

]
