# Generated by Django 4.2.17 on 2025-01-24 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bags', '0009_rename_order_date_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
