# Generated by Django 2.2.24 on 2022-05-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_complaint_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(related_name='_flat_liked_by_+', to='property.User', verbose_name='Понравилось пользователям'),
        ),
    ]
