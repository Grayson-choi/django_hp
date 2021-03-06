from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('ping/', views.ping, name='ping'),
    path('pong/', views.pong, name='pong'),
    path('<int:number>/', views.detail, name='detail')    
]
