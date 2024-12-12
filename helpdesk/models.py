from django.db import models

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Enviado', 'Enviado'),
        ('Pendiente', 'Pendiente'),
        ('Resuelto', 'Resuelto'),
    ]

    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Enviado')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Ticket #{self.id} - {self.name}'
