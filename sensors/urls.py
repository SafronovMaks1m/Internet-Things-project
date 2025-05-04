from django.urls import path, include
from sensors import views

urlsapi = [
    path('sensors/', views.api_sensor, name = 'sensor'),
    path('users/', views.api_data_users, name = 'api_users')
]

urlpatterns = [
    path('', views.base, name = 'base'),
    path('sensors/', views.sensors, name = 'sensors'),
    path('users/', views.users, name = 'users'),
    path('api/', include(urlsapi))
]