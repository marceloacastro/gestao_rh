# Generated by Django 3.2.4 on 2021-06-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0002_registrohoraextra_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='horas',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
