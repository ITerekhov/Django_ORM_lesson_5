from django.db import migrations
from django.db.models import F

def filled_new_building_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.update(new_building = F('construction_year') >= 2015)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(filled_new_building_field),
    ]
