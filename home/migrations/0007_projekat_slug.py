# Generated by Django 5.0.6 on 2024-05-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_tehnologija_remove_projekat_pretplata_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projekat',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
