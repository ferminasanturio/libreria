# Generated by Django 4.2.3 on 2023-08-19 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_articulo_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='subtitulo',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='titulo',
            field=models.CharField(max_length=256),
        ),
    ]
