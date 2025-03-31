from django.urls import path
from .views import home, register_view, login_view, logout_view, create_patient, update_patient, delete_patient, doctor_list, create_doctor, patient_list

urlpatterns = [
    path('', patient_list, name='home'),  # Add a name for this route
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('doctor/', doctor_list, name='doctor'),
    path('create-patient/', create_patient, name='create-patient'),
    path('update-patient/<int:pk>/', update_patient, name='update-patient'),
    path('delete-patient/<int:pk>/', delete_patient, name='delete-patient'),
    path('create-doctor/', create_doctor, name='create-doctor'),
]
