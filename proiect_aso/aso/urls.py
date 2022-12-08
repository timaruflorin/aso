from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/<slug:slug>/', views.room, name='room'),
    path('createroom/',views.createroom,name='createroom'),
]
