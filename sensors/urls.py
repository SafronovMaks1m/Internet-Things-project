from django.urls import path, include
from django.views.generic import TemplateView
from sensors import views

urlpatterns = [
    path('', views.base, name = 'blog'),
    path('api/sensors/', views.sensor, name = 'sensor')
]