# Generated by Django 4.1.4 on 2024-01-20 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0007_employee_employeephotourl"),
    ]

    operations = [
        migrations.RemoveField(model_name="employee", name="EmployeePhotoURL",),
        migrations.RemoveField(model_name="employee", name="user",),
    ]
