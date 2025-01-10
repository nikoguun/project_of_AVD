# Generated by Django 5.1.4 on 2025-01-08 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_analyzer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSVFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='csv_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
