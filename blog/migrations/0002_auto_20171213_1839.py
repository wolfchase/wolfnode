# Generated by Django 2.0 on 2017-12-14 02:39

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
