# Generated by Django 5.1 on 2024-08-23 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('short_polling', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
