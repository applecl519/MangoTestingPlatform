# Generated by Django 4.1.5 on 2023-05-19 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_ui', '0004_uicasegroup_case_people_uicasegroup_timing_actuator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runsort',
            name='ass_type',
            field=models.CharField(max_length=1048, null=True, verbose_name='断言类型'),
        ),
        migrations.AlterField(
            model_name='runsort',
            name='ope_type',
            field=models.CharField(max_length=1048, null=True, verbose_name='对该元素的操作类型'),
        ),
    ]
