# Generated by Django 3.2.3 on 2021-10-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default=12321435343, max_length=50),
            preserve_default=False,
        ),
    ]
