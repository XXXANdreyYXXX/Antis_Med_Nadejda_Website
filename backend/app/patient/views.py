from django.shortcuts import render

# Create your views here.
def main_data_view(request, patient_id):
    return render('basic_patient_data/index.html')