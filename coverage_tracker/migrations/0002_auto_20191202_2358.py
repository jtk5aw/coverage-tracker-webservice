# Generated by Django 2.2.5 on 2019-12-03 04:58

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('coverage_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffer',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='5714395221', max_length=128, region=None),
        ),
    ]
