# Generated by Django 3.0.7 on 2020-06-29 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stable', models.BooleanField()),
                ('gross_weight', models.DecimalField(decimal_places=3, max_digits=7)),
                ('tare', models.DecimalField(decimal_places=3, max_digits=7)),
                ('net_weight', models.DecimalField(decimal_places=3, max_digits=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('identification', models.CharField(max_length=30)),
                ('min_acceptation', models.DecimalField(decimal_places=3, max_digits=7)),
                ('max_acceptation', models.DecimalField(decimal_places=3, max_digits=7)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='balance.Equipment')),
                ('weight', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='balance.Weight')),
            ],
        ),
    ]
