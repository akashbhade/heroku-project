from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
]