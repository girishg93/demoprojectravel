# Generated by Django 4.1.3 on 2022-11-22 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='desc1',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='img1',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='name1',
            new_name='name',
        ),
    ]
