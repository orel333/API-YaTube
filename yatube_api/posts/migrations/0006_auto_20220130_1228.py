# Generated by Django 2.2.16 on 2022-01-30 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220129_2137'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='not_for_self',
        ),
    ]