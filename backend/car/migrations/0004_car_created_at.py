# Generated by Django 4.1.6 on 2023-11-23 14:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("car", "0003_alter_car_carrying_capacity"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
