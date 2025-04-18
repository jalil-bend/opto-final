# Generated by Django 5.0 on 2025-03-14 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0011_initial_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('details', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='medical_records/%Y/%m/%d/')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to='users.patient')),
                ('professional', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_records', to='users.professional')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='MedicalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('topographie', 'Topographie'), ('oct', 'OCT'), ('lampe_a_fente', 'Lampe à fente')], max_length=20)),
                ('image', models.ImageField(upload_to='medical_records/images/%Y/%m/%d/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='records.medicalrecord')),
            ],
            options={
                'ordering': ['category', 'uploaded_at'],
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('medication', models.CharField(max_length=255)),
                ('dosage', models.CharField(max_length=255)),
                ('instructions', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
        ),
    ]
