from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PatientForm, DoctorForm
from .models import Patient, Doctor

@login_required
# Create your views here.
def home(request):
    # return HttpResponse("Hello, world. You're at the user home page.")
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        # Handle form submission
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                # Create a new user
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                return redirect('home')  # Redirect to home page after successful registration
                # return HttpResponse("User registered successfully!")
            except:
                message.error(request, "Username already exists!")
        else:
            messages.error(request, "Passwords do not match!")
    #     # Render the registration form
    return render(request, 'registration/register.html')

def login_view (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid username or password!")
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to home page after logout

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm()
    return render(request, "patient/create_patient.html", {'form': form})
    # return render(request, 'create_patient.html', {'form': form})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'home.html', {'patients': patients})

def update_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient/update_patient.html', {'form': form})

def delete_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return redirect('home')


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor.html', {'doctors': doctors})

def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor/doctor.html')
    else:
        form = DoctorForm()
    return render(request, "doctor/create_doctor.html", {'form': form})