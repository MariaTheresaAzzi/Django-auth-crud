from django import forms
from .models import Doctor, Patient

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        # fields = ['doctor_id', 'firstname', 'lastname', 'specialization', 'department']
        fields = '__all__'
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'patient_id': forms.TextInput(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
        }