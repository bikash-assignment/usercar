# Generated by Django 3.1.1 on 2020-09-13 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_remove_car_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]