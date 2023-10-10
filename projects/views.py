from django.shortcuts import render, redirect
from .forms import proj_Form
from .models import *
from staff.models import *

from django.contrib import messages

# Create your views here.
def project_view(request, column_name):
    model=column_name+'_Images'
    model=globals()[model]
    context={
        'corousel_images':list(Corousel_Images.objects.values_list('corousel_images',  'corousel_type')),   
        'images':model.objects.values_list(column_name, flat=True),
        'type':column_name
    }
   
    return render(request, 'projects/project.html', context)

def request_project(request):
    context={
        'corousel_images':list(Corousel_Images.objects.values_list('corousel_images',  'corousel_type')),   
        'form':proj_Form()
    }
    if request.method == 'POST':
        form = proj_Form(request.POST)
        if form.is_valid():
            phone_Number=form.cleaned_data['phone_number']
            if project.objects.filter(phone_number=phone_Number).exists() or projectapproved.objects.filter(phone_number=phone_Number).exists():
                messages.error(request, 'phone_number exists')
            else:
                form.save()
                messages.success(request, 'Application saved successfully')
                return redirect('project', column_name='Upcoming_Project')  # Redirect to a success page or any other appropriate URL
        else:
            error=str(form.errors)
            messages.error(request, error)
    return render(request, 'projects/request.html', context)
