# Generated by Django 5.1.4 on 2025-01-25 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mess_owner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mess',
            old_name='mess_photo',
            new_name='mess_image',
        ),
    ]
