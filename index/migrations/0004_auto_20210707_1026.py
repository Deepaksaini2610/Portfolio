# Generated by Django 3.1.1 on 2021-07-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='slides',
            field=models.ImageField(upload_to='slid/'),
        ),
    ]
