from django.shortcuts import render, redirect
from .forms import opp_Form
from .models import *
from django.db.models import Count, Sum
from staff.models import Corousel_Images
from django.contrib import messages

def oppotunity(request):
    context={
    'corousel_images':list(Corousel_Images.objects.values_list('corousel_images',  'corousel_type')),
    'form':opp_Form()
    }
    if request.method == 'POST':
        form = opp_Form(request.POST)
        if form.is_valid():
            phone_Number=form.cleaned_data['phone_number']
            if oppotunities.objects.filter(phone_number=phone_Number).exists() or oppotunitiesapproved.objects.filter(phone_number=phone_Number).exists():
                messages.error(request, 'phone_number exists')   
            else:
                form.save()
                messages.success(request, 'Application saved successfully')
                return redirect('oppotunity_sta')  # Redirect to a success page or any other appropriate URL
        else:
            error=str(form.errors)
            messages.error(request, error)    
      # If it's a GET request or form is not val
    return render(request, 'oppotunities/oppotunities.html', context)



def oppotunity_sta(request):
    count=oppotunities.objects.aggregate(name_count=Count('name'))
    count=count['name_count']
    approved=oppotunitiesapproved.objects.aggregate(name_count=Count('name'))
    approved=approved['name_count']
    count=count +  approved
    if approved!=0:
        percentage= round( (approved/count)*100)
    else:
        percentage=0
    context={
    'count':count,
    'approved':approved,
    'percentage':percentage,
    'corousel_images':list(Corousel_Images.objects.values_list('corousel_images',  'corousel_type')),     
    }
    return render(request, 'oppotunities/statistics.html',  context)




