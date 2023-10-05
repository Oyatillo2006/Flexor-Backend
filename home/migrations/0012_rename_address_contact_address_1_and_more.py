# Generated by Django 4.2.5 on 2023-09-27 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='address',
            new_name='address_1',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='emai_1',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='tel',
            new_name='tel_1',
        ),
        migrations.AddField(
            model_name='contact',
            name='address_2',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='emai_2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='tel_2',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]