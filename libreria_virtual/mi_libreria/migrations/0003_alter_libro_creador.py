# Generated by Django 4.2.3 on 2023-08-15 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mi_libreria', '0002_alter_libro_creador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='creador',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='libros_creados', to=settings.AUTH_USER_MODEL),
        ),
    ]
