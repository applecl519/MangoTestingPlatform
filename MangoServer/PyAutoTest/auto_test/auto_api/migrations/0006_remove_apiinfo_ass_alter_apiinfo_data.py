# Generated by Django 4.1.5 on 2023-12-12 10:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auto_api', '0005_apiinfo_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apiinfo',
            name='ass',
        ),
        migrations.AlterField(
            model_name='apiinfo',
            name='data',
            field=models.JSONField(null=True, verbose_name='data'),
        ),
    ]
