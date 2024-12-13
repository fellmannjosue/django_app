# Generated by Django 5.1.4 on 2024-12-13 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Red y Seguridad', 'Red y Seguridad'), ('Sistema de comunicación', 'Sistema de comunicación'), ('Proyección audiovisual', 'Proyección audiovisual'), ('Equipos de informática', 'Equipos de informática'), ('Pantallas digitales', 'Pantallas digitales'), ('Equipos de impresión', 'Equipos de impresión'), ('Enrutadores de red', 'Enrutadores de red')], max_length=50)),
                ('details', models.TextField()),
            ],
        ),
    ]
