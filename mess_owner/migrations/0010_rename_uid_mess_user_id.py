# Generated by Django 5.1.4 on 2025-02-07 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mess_owner', '0009_rename_user_id_mess_uid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mess',
            old_name='uid',
            new_name='user_id',
        ),
    ]
