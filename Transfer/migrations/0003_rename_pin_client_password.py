# Generated by Django 4.0.6 on 2022-09-21 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Transfer', '0002_client_email_client_first_name_client_last_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='pin',
            new_name='password',
        ),
    ]
