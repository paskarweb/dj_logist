from django.urls import path
from . import views

urlpatterns = [
    path('', views.show),
    path('clients/', views.client_list),
    #path( '<int:ruЬric_id>/', Ьy_ruЬric),
    #path (' ', index),
]
