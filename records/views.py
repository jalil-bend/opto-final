from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MedicalRecord, MedicalImage, Prescription
from users.models import Patient, Professional
from django.core.exceptions import PermissionDenied

@login_required
def upload_record(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if not hasattr(request.user, 'professional'):
        raise PermissionDenied

    if request.method == 'POST':
        record = MedicalRecord.objects.create(
            patient=patient,
            professional=request.user.professional,
            description=request.POST.get('description', ''),
            diabetique=bool(request.POST.get('diabetique')),
            keratoconique=bool(request.POST.get('keratoconique')),
            cataracte=bool(request.POST.get('cataracte'))
        )

        if request.FILES.get('file'):
            record.file = request.FILES['file']
            record.save()

        # Gérer les images multiples pour chaque catégorie
        categories = ['topographie', 'oct', 'lampe_a_fente']
        for category in categories:
            files = request.FILES.getlist(f'{category}[]')
            for image_file in files:
                MedicalImage.objects.create(
                    record=record,
                    category=category,
                    image=image_file
                )

        # Log des données de prescription
        print("Données de prescription reçues :", {
            'od_sph_lc': request.POST.get('od_sph_lc'),
            'od_cyl_lc': request.POST.get('od_cyl_lc'),
            'od_axe_lc': request.POST.get('od_axe_lc'),
            'od_dia': request.POST.get('od_dia'),
            'od_rc': request.POST.get('od_rc'),
            'og_sph_lc': request.POST.get('og_sph_lc'),
            'og_cyl_lc': request.POST.get('og_cyl_lc'),
            'og_axe_lc': request.POST.get('og_axe_lc'),
            'og_dia': request.POST.get('og_dia'),
            'og_rc': request.POST.get('og_rc')
        })

        # Enregistrer les prescriptions
        Prescription.objects.create(
            record=record,
            od_sph=request.POST.get('od_sph', ''),
            od_cyl=request.POST.get('od_cyl', ''),
            od_axe=request.POST.get('od_axe', ''),
            og_sph=request.POST.get('og_sph', ''),
            og_cyl=request.POST.get('og_cyl', ''),
            og_axe=request.POST.get('og_axe', ''),
            od_sph_lc=request.POST.get('od_sph_lc', ''),
            od_cyl_lc=request.POST.get('od_cyl_lc', ''),
            od_axe_lc=request.POST.get('od_axe_lc', ''),
            od_dia=request.POST.get('od_dia', ''),
            od_rc=request.POST.get('od_rc', ''),
            og_sph_lc=request.POST.get('og_sph_lc', ''),
            og_cyl_lc=request.POST.get('og_cyl_lc', ''),
            og_axe_lc=request.POST.get('og_axe_lc', ''),
            og_dia=request.POST.get('og_dia', ''),
            og_rc=request.POST.get('og_rc', '')
        )

        messages.success(request, 'Dossier médical créé avec succès.')
        return redirect('view_records', patient_id=patient.id)

    return render(request, 'records/upload_record.html', {'patient': patient})

@login_required
def patient_records(request):
    if not hasattr(request.user, 'patient'):
        raise PermissionDenied
    
    patient = request.user.patient  # Get the patient instance
    records = MedicalRecord.objects.filter(patient=patient)
    return render(request, 'records/patient_records.html', {
        'records': records,
        'patient': patient,  # Pass the patient instance to the template
        'date_of_birth': patient.date_of_birth  # Pass the patient's date of birth to the template
    })

@login_required
def view_records(request, patient_id):
    # Cette vue est maintenant réservée aux professionnels
    if not hasattr(request.user, 'professional'):
        raise PermissionDenied
        
    patient = get_object_or_404(Patient, id=patient_id)
    records = MedicalRecord.objects.filter(patient=patient).prefetch_related('prescriptions')
    
    return render(request, 'records/view_records.html', {
        'patient': patient,
        'records': records,
    })

@login_required
def create_prescription(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if not hasattr(request.user, 'professional'):
        raise PermissionDenied

    if request.method == 'POST':
        medicaments = request.POST.getlist('medicament')
        dosages = request.POST.getlist('dosage')
        frequences = request.POST.getlist('frequence')
        details = []
        for med, dose, freq in zip(medicaments, dosages, frequences):
            if med:
                details.append(f"{med} | {dose} | {freq} fois/jour")

        record = MedicalRecord.objects.filter(patient=patient).order_by('-created_at').first()
        if not record:
            record = MedicalRecord.objects.create(patient=patient, professional=request.user.professional)
        Prescription.objects.create(record=record, prescription_details="; ".join(details))
        messages.success(request, "Ordonnance créée avec succès.")
        return redirect('view_records', patient_id=patient.id)

    return render(request, 'records/create_prescription.html', {'patient': patient})
