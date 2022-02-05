from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

  path('search/', views.searchBar, name='search'),

  # path('', views.home, name="home"),
  path('student/', views.student, name="student"),
  path('', views.dashboard, name="dashboard"),
]