# Generated by Django 4.1.5 on 2024-10-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_system', '0006_database_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledtasks',
            name='cron',
            field=models.CharField(max_length=64, null=True, verbose_name='cron表达式'),
        ),
    ]
