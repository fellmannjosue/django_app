from django.urls import path
from . import views

urlpatterns = [
    path('', views.maintenance_home, name='maintenance_home'),
]
