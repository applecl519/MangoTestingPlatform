# Generated by Django 4.1.5 on 2023-05-04 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto_ui', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runsort',
            name='team',
        ),
    ]
