# Generated by Django 4.1.4 on 2024-01-20 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0010_alter_performance_employee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="performance",
            name="Employee",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="pages.employee"
            ),
        ),
    ]
