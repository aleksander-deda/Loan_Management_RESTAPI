# Generated by Django 4.1.3 on 2023-01-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('underwriters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='underwriter',
            name='code',
            field=models.CharField(blank=True, max_length=5, null=True, unique=True),
        ),
    ]