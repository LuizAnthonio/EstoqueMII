# Generated by Django 4.2.3 on 2023-09-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='porcao',
            field=models.IntegerField(default=1),
        ),
    ]
