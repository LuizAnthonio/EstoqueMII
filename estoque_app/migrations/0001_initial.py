# Generated by Django 4.2.3 on 2023-08-24 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id_uni', models.AutoField(primary_key=True, serialize=False)),
                ('alimento', models.TextField(max_length=255)),
                ('quantidade_qtd', models.FloatField()),
                ('validade', models.DateField()),
                #('porcao', models.FloatField())
            ],
        ),
    ]
