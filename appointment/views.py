

from django.shortcuts import render, redirect
from .forms import app_Form
from .models import appointment, appointmentapproved
from staff.models import Corousel_Images
from django.contrib import messages



def book_appointment(request):
    context={
    'corousel_images':list(Corousel_Images.objects.values_list('corousel_images',  'corousel_type')),
    'form':app_Form()
    }
    if request.method == 'POST':
        form = app_Form(request.POST)
        if form.is_valid():
            phone_Number=form.cleaned_data['phone_number']
            if appointment.objects.filter(phone_number=phone_Number).exists() or appointmentapproved.objects.filter(phone_number=phone_Number).exists():
                messages.error(request, 'phone_number exists') 
            else:
                form.save()
                messages.success(request, 'Application saved successfully')                
                return redirect('home')   
        else:
            error=str(form.errors)
            messages.error(request, error)
            # Redirect to a success page or any other appropriate URL
      # If it's a GET request or form is not valid
    return render(request, 'appointment/book_appointment.html', context)








