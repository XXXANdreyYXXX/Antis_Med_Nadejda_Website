from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def view_department(request):
    context = {'title': 'Отделение'}
    return render(request, 'department/department.html', context)
