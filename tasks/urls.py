from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('',views.HomeView,name="home"),
   path('list/',views.index,name="list"),
   path('update_task/<str:pk>/',views.UpdateTask,name="update_task"),
   path('delete/<str:pk>/',views.deleteTask,name="delete"),
    path('login/',views.LoginView,name='login'),
    path('register/',views.RegisterView,name='register'),
    path('logout/',views.LogoutView,name='logout'),
]
