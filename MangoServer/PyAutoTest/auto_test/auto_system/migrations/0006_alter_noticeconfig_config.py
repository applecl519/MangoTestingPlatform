# Generated by Django 4.1.5 on 2023-05-19 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_system', '0005_testobject_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticeconfig',
            name='config',
            field=models.CharField(max_length=1028, null=True, verbose_name='通知配置'),
        ),
    ]
