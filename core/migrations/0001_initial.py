# Generated by Django 5.1 on 2024-09-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poeme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('contenu', models.TextField()),
                ('langue', models.CharField(choices=[('fr', 'Français'), ('pt', 'Portugais'), ('bi', 'Bilingue')], max_length=2)),
                ('auteur', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('langue', models.CharField(choices=[('fr', 'Français'), ('pt', 'Portugais'), ('bi', 'Bilingue')], max_length=2)),
                ('lieu', models.CharField(choices=[('int', 'Intérieur'), ('ext', 'Extérieur')], max_length=3)),
                ('musique', models.BooleanField(default=False)),
                ('fichier', models.FileField(upload_to='videos/')),
            ],
        ),
    ]
