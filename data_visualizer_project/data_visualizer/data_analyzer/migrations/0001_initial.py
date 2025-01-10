# Generated by Django 5.1.4 on 2025-01-08 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fichier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('fichier', models.FileField(upload_to='uploads/')),
                ('date_upload', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]