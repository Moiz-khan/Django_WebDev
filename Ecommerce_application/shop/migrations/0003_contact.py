# Generated by Django 3.2.3 on 2021-10-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210904_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(max_length=300)),
            ],
        ),
    ]
