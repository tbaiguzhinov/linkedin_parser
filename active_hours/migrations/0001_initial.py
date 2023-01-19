# Generated by Django 3.2.16 on 2023-01-19 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=1000, verbose_name='Contact name')),
                ('occupation', models.CharField(max_length=1000, verbose_name='Occupation')),
            ],
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_time', models.DateTimeField(verbose_name='Time logged')),
                ('status', models.CharField(max_length=1000, verbose_name='Presence status')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presence_hours', to='active_hours.contact')),
            ],
        ),
    ]
