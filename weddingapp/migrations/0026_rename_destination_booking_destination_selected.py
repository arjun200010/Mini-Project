# Generated by Django 4.2.2 on 2023-11-19 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weddingapp', '0025_booking_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='destination',
            new_name='destination_selected',
        ),
    ]
