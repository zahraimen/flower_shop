# Generated by Django 4.0.4 on 2022-06-14 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0012_alter_flower_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='seller',
            field=models.CharField(max_length=225),
        ),
    ]