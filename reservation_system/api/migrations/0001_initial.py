# Generated by Django 5.1.4 on 2024-12-19 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateField()),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('IN_PROGRESS', 'IN_PROGRESS'), ('COMPLETED', 'COMPLETED'), ('CANCELED', 'CANCELED'), ('NO_SHOW', 'NO_SHOW')], max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.client')),
            ],
        ),
    ]
