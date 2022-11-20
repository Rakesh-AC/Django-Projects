from django.contrib import admin
from django.urls import path
from userapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='name'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logOut, name='logout'),
    path('profile/', views.profile, name='profile'),
]