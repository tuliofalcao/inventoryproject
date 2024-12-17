# Generated by Django 5.1.2 on 2024-12-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('categoria', models.CharField(choices=[('Eletronicos', 'Eletronicos'), ('Alimento', 'Alimento'), ('Estacionario', 'Estacionario')], max_length=20, null=True)),
                ('quantidade', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
