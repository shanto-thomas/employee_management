# Generated by Django 4.0.6 on 2022-07-22 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0005_employee_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='text',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]