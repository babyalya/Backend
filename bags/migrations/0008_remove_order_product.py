# Generated by Django 4.2.17 on 2025-01-23 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bags', '0007_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]
