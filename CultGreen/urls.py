from django.urls import path
from . import views

urlpatterns = [
    path ('', views.welcome, name="welcome"),
    
    path ('home/', views.home, name="home"),

    path ('search/', views.search, name="search"),

    path ('about/', views.about, name="about"),

    path ('myplants/', views.myplants, name="myplants"),

    path('add/', views.add_plant, name='add_plant'),

    path('edit/<int:pk>/', views.edit_plant, name='edit_plant'),
    
     path('delete/<int:pk>/', views.delete_plant, name='delete_plant'),

    path ('login/', views.login, name="login"),

     path ('signup/', views.signup, name="signup"),
]
