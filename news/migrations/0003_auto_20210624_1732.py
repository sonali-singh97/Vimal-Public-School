# Generated by Django 3.2.2 on 2021-06-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210617_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='url',
            new_name='pdf',
        ),
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
