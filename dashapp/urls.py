from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dash/', views.DashView, name='room'),
    path('add/', views.AddView)
]
