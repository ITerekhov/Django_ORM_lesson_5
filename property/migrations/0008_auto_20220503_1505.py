# Generated by Django 2.2.24 on 2022-05-03 12:05

from django.db import migrations

import phonenumbers


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(phone):
            flat.owner_pure_phone = phone
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers)
    ]
