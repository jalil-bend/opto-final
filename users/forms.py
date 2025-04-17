from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User, Patient, Researcher

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': "Nom d'utilisateur",
            'email': 'Email',
            'first_name': 'Prénom',
            'last_name': 'Nom'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['date_of_birth', 'gender']
        labels = {
            'date_of_birth': 'Date de naissance',
            'gender': 'Sexe'
        }
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'gender': forms.Select(attrs={'class': 'form-control'})
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nom')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')

class AccessCodeForm(forms.Form):
    access_code = forms.CharField(label='Code d\'accès', max_length=8)

# Nouveau formulaire pour la génération de code
class GenerateAccessCodeForm(forms.Form):
    duration_hours = forms.IntegerField(
        label='Durée de validité (en heures)',
        min_value=1,
        initial=24,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '1'
        })
    )

class ResearcherCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    license_number = forms.CharField(required=True, max_length=50)
    research_domain = forms.CharField(required=True, max_length=100)
    current_projects = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'license_number', 'research_domain', 'current_projects')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_researcher = True
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            researcher = Researcher.objects.create(
                user=user,
                license_number=self.cleaned_data['license_number'],
                research_domain=self.cleaned_data['research_domain'],
                current_projects=self.cleaned_data['current_projects']
            )
        return user
