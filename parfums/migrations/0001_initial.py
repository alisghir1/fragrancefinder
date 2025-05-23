# Generated by Django 5.1.6 on 2025-02-27 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parfum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('marque', models.CharField(max_length=255)),
                ('genre', models.CharField(choices=[('men', 'Homme'), ('women', 'Femme'), ('unisex', 'Unisexe')], max_length=50)),
                ('annee', models.IntegerField(blank=True, null=True)),
                ('notes_tete', models.TextField(blank=True, null=True)),
                ('notes_coeur', models.TextField(blank=True, null=True)),
                ('notes_fond', models.TextField(blank=True, null=True)),
                ('accords_principaux', models.TextField(blank=True, null=True)),
                ('note_moyenne', models.FloatField(blank=True, null=True)),
                ('nombre_votes', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
