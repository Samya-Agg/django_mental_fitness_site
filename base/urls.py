from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('chat/',views.chatting,name="chatting"),
    path('register/',views.reg,name="reg"),
    path('login/',views.loginPage,name="loginPage"),
    path('logout/',views.logoutpage,name="logout"),
    path('profile/',views.account,name="profile"),
    path('home/',views.index,name="home"),

]
