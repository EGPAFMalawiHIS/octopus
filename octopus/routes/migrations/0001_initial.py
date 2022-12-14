# Generated by Django 3.2.16 on 2022-10-19 17:05

from django.db import migrations, models
import octopus.routes.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', octopus.routes.models.UuidField(default=uuid.uuid4, max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='The name of the route.', max_length=255, null=True)),
                ('description', models.TextField(blank=True, help_text='Description of the route. For example SMS route or MoH WAN route.', null=True)),
                ('type', models.CharField(choices=[('Internet', 'Internet'), ('VPN', 'VPN'), ('SMS', 'SMS')], max_length=255, null=True)),
                ('weight', models.IntegerField(default=1, help_text='A route should have a unique weighting. No two routes can have same weighting.', unique=True)),
                ('status', models.CharField(blank=True, choices=[('Up', 'Up'), ('Down', 'Down'), ('Unknown', 'Unknown')], default='Unknown', max_length=255, null=True)),
                ('address', models.CharField(blank=True, help_text='This can be a default gateway or anything similar that can ascertain if a route is UP.', max_length=255, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
