# Generated by Django 5.0.4 on 2024-05-14 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='Productos', to='api.categoria'),
        ),
    ]
