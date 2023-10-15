
from django.shortcuts import render,redirect
from .models import *
from staff.models import Corousel_Images
from django.contrib import messages
from .forms import Prof_Form

# Create your views here.

def proffessionals(request):
    context={
    'corousel_images':list(Corousel_Images.objects.values_list('Corousel',  'corousel_type')),
    'form':Prof_Form()
}
    return render(request, 'proffesional/proffesionals.html', context )


def prof_rejister(request):
    context={
    'corousel_images':list(Corousel_Images.objects.values_list('Corousel',  'corousel_type')),
    'form':Prof_Form()
}
    if request.method == 'POST':
        form=Prof_Form(request.POST)
        if form.is_valid():
            phone_Number=form.cleaned_data['phone_number']
            if Proffession.objects.filter(phone_number=phone_Number).exists() or Proffessionapproved.objects.filter(phone_number=phone_Number).exists():
                messages.error(request,
                                 'error phone_number exists')
            else:
                form.save()
                messages.success(request, 'Application saved successfully')
                return redirect('proffessionals' )
            
        else:
            error=str(form.errors)
            messages.error(request, error)
    return render(request, 'proffesional/rejister.html', context
                  )
