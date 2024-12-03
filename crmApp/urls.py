from django.urls import path
from .views import home, register,login,dashboard,logout,create_record, update_record


urlpatterns = [
    path('', home, name=''),

    path('register/', register, name='register' ),

    path('login/', login, name='login' ),

    path('logout/', logout, name='logout' ),

    path('dashboard/', dashboard, name='dashboard' ),

    path('create_record/', create_record, name='create_record' ),

    path('update_record/<int:pk>/', update_record, name='update_record' ),

]
