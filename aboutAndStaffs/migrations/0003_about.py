# Generated by Django 3.0.5 on 2021-06-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aboutAndStaffs', '0002_auto_20210607_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
