# Generated by Django 4.1.5 on 2023-12-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auto_api', '0015_apicase_module_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiresult',
            name='error_message',
            field=models.CharField(max_length=1024, null=True, verbose_name='失败原因'),
        ),
    ]