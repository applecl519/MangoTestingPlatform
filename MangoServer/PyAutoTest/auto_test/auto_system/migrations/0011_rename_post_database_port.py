# Generated by Django 4.1.5 on 2023-11-20 06:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('auto_system', '0010_rename_state_database_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='database',
            old_name='post',
            new_name='port',
        ),
    ]
