# Generated by Django 3.2.4 on 2021-06-13 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0002_departamento_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='nome',
            field=models.CharField(max_length=70),
        ),
    ]
