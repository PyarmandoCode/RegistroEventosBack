# Generated by Django 3.2.16 on 2022-12-19 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Departamentos',
        ),
        migrations.DeleteModel(
            name='Estacionamiento',
        ),
        migrations.AddField(
            model_name='eventos',
            name='eventos_nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
