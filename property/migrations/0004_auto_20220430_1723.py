from django.db import migrations


def filled_new_building_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = flat.construction_year >= 2015
        flat.save()

        
class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(filled_new_building_field),
    ]
