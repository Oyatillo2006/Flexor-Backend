# Generated by Django 4.2.5 on 2023-09-27 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_emai_1_contact_email_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email_1',
            new_name='docs',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email_2',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='tel_1',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='tel_2',
        ),
    ]
