# Generated by Django 4.2.2 on 2023-11-03 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingapp', '0006_package_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='goldpackage',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
