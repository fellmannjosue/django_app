from django.urls import path
from . import views

urlpatterns = [
    path('', views.maintenance_dashboard, name='maintenance_dashboard'),
    path('download_maintenance_pdf/<int:record_id>/', views.download_maintenance_pdf, name='download_maintenance_pdf'),
]
