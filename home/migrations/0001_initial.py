# Generated by Django 5.0.6 on 2024-05-27 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.TextField()),
                ('platforma', models.CharField(max_length=255)),
                ('datum_pocetka', models.DateField()),
                ('datum_zavrsetka', models.DateField(blank=True, null=True)),
                ('sertifikat', models.BooleanField(default=False)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projekat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.TextField()),
                ('datum_pocetka', models.DateField()),
                ('datum_zavrsetka', models.DateField(blank=True, null=True)),
                ('tehnologije', models.CharField(max_length=255)),
                ('link', models.URLField(blank=True, null=True)),
                ('slika', models.ImageField(blank=True, null=True, upload_to='projekti/')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
                ('opis', models.TextField()),
                ('video_url', models.URLField()),
                ('redni_broj', models.IntegerField()),
                ('kurs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levele', to='home.kurs')),
            ],
            options={
                'ordering': ['redni_broj'],
                'unique_together': {('kurs', 'redni_broj')},
            },
        ),
    ]
