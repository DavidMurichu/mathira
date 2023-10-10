from django.shortcuts import render,redirect
from .models import *
from staff.models import Corousel_Images
from django.contrib import messages
from .forms import diasp_Form

# Create your views here.

def diaspora_affairs(request):
    context={
    'corousel_images':list(Corousel_Images.objects.values_list('corousel_images',  'corousel_type')),
    'form':diasp_Form()
}
    return render(request, 'diaspora/affairs.html', context)

def diaspora_register(request):
    context={
    'corousel_images':list(Corousel_Images.objects.values_list('corousel_images',  'corousel_type')),
    'form':diasp_Form()
}
    if request.method == 'POST':
        form = diasp_Form(request.POST)
        if form.is_valid():
            phone_number=form.cleaned_data['phone_number']
            if diaspora.objects.filter(phone_number=phone_number).exists() or diasporaapproved.objects.filter(phone_number=phone_number).exists():
                messages.error(request, 'phone_number exists')
            else:
                form.save()
                messages.success(request, 'Application saved successfully')
                return redirect('diaspora')
        else:
            error=str(form.errors )
            messages.error(request, error)
    return render(request, 'diaspora/diaspora_rejister.html', context)

 