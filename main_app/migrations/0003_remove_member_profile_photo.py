# Generated by Django 2.1.2 on 2018-10-18 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_member_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='profile_photo',
        ),
    ]
