from django.db import models
from users.models import Patient, Professional

# Modèle pour les dossiers médicaux
class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        'users.Patient',
        on_delete=models.CASCADE,
        related_name='medical_records'
    )
    professional = models.ForeignKey(
        'users.Professional',
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_records'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    details = models.TextField()
    file = models.FileField(upload_to='medical_records/%Y/%m/%d/', blank=True, null=True)
    diabetique = models.BooleanField(default=False, verbose_name="Diabétique")
    keratoconique = models.BooleanField(default=False, verbose_name="Kératoconique")
    cataracte = models.BooleanField(default=False, verbose_name="Cataracte")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Dossier de {self.patient.user.username} - {self.created_at.strftime('%Y-%m-%d')}"

# Modèle pour les images médicales
class MedicalImage(models.Model):
    CATEGORY_CHOICES = [
        ('topographie', 'Topographie'),
        ('oct', 'OCT'),
        ('lampe_a_fente', 'Lampe à fente'),
    ]

    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='images')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='medical_records/images/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'uploaded_at']

    def __str__(self):
        return f"{self.get_category_display()} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"

# Modèle pour les prescriptions
class Prescription(models.Model):
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='prescriptions')
    od_sph = models.CharField(max_length=10, blank=True)
    od_cyl = models.CharField(max_length=10, blank=True)
    od_axe = models.CharField(max_length=10, blank=True)
    og_sph = models.CharField(max_length=10, blank=True)
    og_cyl = models.CharField(max_length=10, blank=True)
    og_axe = models.CharField(max_length=10, blank=True)
    od_dia = models.CharField(max_length=10, blank=True)
    od_rc = models.CharField(max_length=10, blank=True)
    og_dia = models.CharField(max_length=10, blank=True)
    og_rc = models.CharField(max_length=10, blank=True)
    od_sph_lc = models.CharField(max_length=10, blank=True)
    od_cyl_lc = models.CharField(max_length=10, blank=True)
    od_axe_lc = models.CharField(max_length=10, blank=True)
    og_sph_lc = models.CharField(max_length=10, blank=True)
    og_cyl_lc = models.CharField(max_length=10, blank=True)
    og_axe_lc = models.CharField(max_length=10, blank=True)
    prescription_details = models.TextField(blank=True)  # Ordonnance médicaments/dosages/fréquences
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Prescription du {self.created_at.strftime('%Y-%m-%d')}"
