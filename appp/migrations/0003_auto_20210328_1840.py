# Generated by Django 3.1.7 on 2021-03-28 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appp', '0002_s_user_types'),
    ]

    operations = [
        migrations.RenameField(
            model_name='s_user',
            old_name='User',
            new_name='user',
        ),
    ]
