# Generated by Django 4.2.3 on 2023-08-19 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_articulo_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='fecha',
            field=models.DateField(),
        ),
    ]
