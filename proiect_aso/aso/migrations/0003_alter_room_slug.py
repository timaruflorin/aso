# Generated by Django 4.0.1 on 2022-12-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aso', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', unique=True),
        ),
    ]