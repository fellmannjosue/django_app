from django.db import models

class InventoryItem(models.Model):
    CATEGORY_CHOICES = [
        ('Red y Seguridad', 'Red y Seguridad'),
        ('Sistema de comunicación', 'Sistema de comunicación'),
        ('Proyección audiovisual', 'Proyección audiovisual'),
        ('Equipos de informática', 'Equipos de informática'),
        ('Pantallas digitales', 'Pantallas digitales'),
        ('Equipos de impresión', 'Equipos de impresión'),
        ('Enrutadores de red', 'Enrutadores de red'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    details = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.category}"
