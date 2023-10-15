
from django.shortcuts import render, redirect
from .forms import contact_Form
from .models import contact_us
from staff.models import *

from django.contrib import messages

def home(request):
    context={

    'corousel_images':list(Corousel_Images.objects.values_list('Corousel',  'corousel_type')),
    'outlook_images':list(Outlook_Images.objects.values_list('Outlook', flat=True)),
    'team_images':list(Team_Images.objects.values_list('Team', 'image_title',
            'image_name')),
    'project_images':list(Project_Images.objects.values_list('Project', flat=True)),
    'event_images':list(Event_Images.objects.values_list('Event', flat=True)),
    'busary_images':list(Busary_Images.objects.values_list('Busary', flat=True))
    }
    return render(request,'nav_bar_url/home.html', context)

def contact_Us(request):
    if request.method == 'POST':
        form = contact_Form(request.POST)
        if form.is_valid():
            phone_Number=form.cleaned_data['phone_number']
            if contact_us.objects.filter(phone_number=phone_Number).exists():
                messages.error(request, 'phone_number exists')
                form = contact_Form()
                return render(request, 'contact_us.html', {'form': form})
            
            else:
                form.save()
                messages.success(request, 'Application saved successfully')
                return redirect('home')  # Redirect to a success page or any other appropriate URL
    else:  # If it's a GET request or form is not valid
        form = contact_Form()

    return render(request, 'contact_us.html', {'form': form})








