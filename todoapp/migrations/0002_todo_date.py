# Generated by Django 5.0.1 on 2024-01-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]