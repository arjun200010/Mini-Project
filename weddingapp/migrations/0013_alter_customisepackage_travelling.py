# Generated by Django 4.2.2 on 2023-11-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingapp', '0012_alter_customisepackage_travelling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customisepackage',
            name='travelling',
            field=models.CharField(max_length=255),
        ),
    ]
