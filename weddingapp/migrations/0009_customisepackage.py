# Generated by Django 4.2.2 on 2023-11-04 04:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weddingapp', '0008_remove_goldpackage_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomisePackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_booking', models.DateField()),
                ('destination_selected', models.CharField(max_length=255)),
                ('honeymoon_destination', models.BooleanField(blank=True, max_length=255, null=True)),
                ('hotel', models.CharField(max_length=255)),
                ('travelling', models.CharField(max_length=255)),
                ('videography', models.CharField(max_length=255)),
                ('location_to_shoot', models.CharField(blank=True, max_length=255, null=True)),
                ('photography', models.CharField(max_length=255)),
                ('guest', models.IntegerField()),
                ('food', models.CharField(max_length=255)),
                ('is_booked', models.BooleanField(default=False)),
                ('total_amount', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
