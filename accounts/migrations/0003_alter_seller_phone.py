# Generated by Django 4.0.4 on 2022-05-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]