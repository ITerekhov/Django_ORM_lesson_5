# Generated by Django 2.2.24 on 2022-05-03 12:53

from django.db import migrations


def fill_owner_with_data(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        full_name = flat.owner
        owners_phonenumber = flat.owners_phonenumber
        owner_pure_phone = flat.owner_pure_phone
        owner, created = Owner.objects.get_or_create(
            full_name=full_name,
            owner_pure_phone=owner_pure_phone,
            owners_phonenumber=owners_phonenumber,
            )
        owner.flats.add(flat)
        owner.save()
            


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20220503_1546'),
    ]

    operations = [
        migrations.RunPython(fill_owner_with_data)
    ]
