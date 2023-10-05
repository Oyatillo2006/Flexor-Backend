# Generated by Django 4.2.5 on 2023-09-27 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_support_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='client',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='date',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='text',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='url',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(default=2, upload_to='images/Portfolio'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
