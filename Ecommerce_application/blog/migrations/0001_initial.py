# Generated by Django 3.2.3 on 2021-10-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('head0', models.CharField(default='', max_length=500)),
                ('head1', models.CharField(default='', max_length=500)),
                ('head2', models.CharField(default='', max_length=500)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
