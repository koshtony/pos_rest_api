# Generated by Django 5.0.1 on 2024-01-09 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_users', '0005_account_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
