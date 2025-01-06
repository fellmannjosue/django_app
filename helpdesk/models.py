from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Enviado')
    comments = models.TextField(blank=True, null=True)  # Campo para comentarios, opcional
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tickets'  # Especifica el nombre correcto de la tabla en la base de datos

    def __str__(self):
        return f'Ticket #{self.id} - {self.name}'
