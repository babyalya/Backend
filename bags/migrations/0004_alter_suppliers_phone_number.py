# Generated by Django 4.2.17 on 2025-01-18 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bags', '0003_alter_suppliers_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliers',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
