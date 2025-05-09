# Generated by Django 5.0 on 2025-03-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_initial_migration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professional',
            name='access_code',
        ),
        migrations.RemoveField(
            model_name='researcher',
            name='accessed_codes',
        ),
        migrations.RemoveField(
            model_name='researcheraccess',
            name='patients',
        ),
        migrations.AddField(
            model_name='researcher',
            name='accessed_professionals',
            field=models.ManyToManyField(related_name='researchers', through='users.ResearcherAccess', to='users.professional'),
        ),
    ]
