# Generated by Django 4.1.5 on 2024-12-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_ui', '0002_rename_create_time_page_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagesteps',
            name='result_data',
            field=models.JSONField(null=True, verbose_name='测试结果'),
        ),
    ]
