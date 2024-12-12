from django.urls import path
from . import views

urlpatterns = [
    path('submit_ticket/', views.submit_ticket, name='submit_ticket'),
    path('success/', views.success, name='success'),
]
