# Generated by Django 2.0 on 2017-12-15 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171213_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='edited_date',
            new_name='edit_date',
        ),
    ]
