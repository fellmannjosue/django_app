from django.urls import path
from . import views

urlpatterns = [
    path('submit_ticket/', views.submit_ticket, name='submit_ticket'),
    path('success/', views.success, name='success'),
    path('technician_dashboard/', views.technician_dashboard, name='technician_dashboard'),
    path('update_ticket/<int:ticket_id>/', views.update_ticket, name='update_ticket'),
]
