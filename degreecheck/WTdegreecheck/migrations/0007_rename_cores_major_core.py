# Generated by Django 4.2.6 on 2023-10-23 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WTdegreecheck', '0006_auto_20231008_2038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='major',
            old_name='cores',
            new_name='core',
        ),
    ]