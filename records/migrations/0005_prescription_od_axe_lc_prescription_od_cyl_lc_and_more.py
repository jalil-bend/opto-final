# Generated by Django 5.0 on 2025-03-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_prescription_od_dia_prescription_od_rc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='od_axe_lc',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='prescription',
            name='od_cyl_lc',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='prescription',
            name='od_sph_lc',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='prescription',
            name='og_axe_lc',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='prescription',
            name='og_cyl_lc',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='prescription',
            name='og_sph_lc',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
