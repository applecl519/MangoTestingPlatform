# Generated by Django 4.1.5 on 2023-10-23 06:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('auto_system', '0003_remove_tasksruncaselist_case_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scheduledtasks',
            old_name='task_name',
            new_name='name',
        ),
    ]
