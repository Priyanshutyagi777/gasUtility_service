from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_request, name='create_request'),
    path('track/', views.track_requests, name='track_requests'),
]
