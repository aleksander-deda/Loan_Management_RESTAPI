# Generated by Django 4.1.3 on 2023-01-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanagers', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmanager',
            name='code',
            field=models.CharField(blank=True, max_length=5, null=True, unique=True),
        ),
    ]