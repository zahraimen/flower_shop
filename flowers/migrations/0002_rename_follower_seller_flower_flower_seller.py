# Generated by Django 4.0.4 on 2022-05-20 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flower',
            old_name='follower_seller',
            new_name='flower_seller',
        ),
    ]