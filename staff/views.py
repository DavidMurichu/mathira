from django.shortcuts import render, redirect, get_object_or_404
import os
from appointment.models import *
from overseas.models import *
from oppotunity.models import *
from proffessionals.models import *
from projects.models import *
from .models import *


from django.contrib.auth.decorators import login_required
from busary.models import *
from busary.forms import Bus_Form
from .forms import *
from django.contrib import messages


# Create your views here.
@login_required(login_url='/auth/login')
def staff_page(request):
    return render(request, 'staff/staff.html')

@login_required(login_url='/auth/login')
def Delete(request, id, model):
    prev_url= request.META.get('HTTP_REFERER', None)
    model=globals()[model]
    Object=model.objects.get(pk=id)
    Object.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect(prev_url)



# def delete(request, id, model): 
#     model = globals()[model]
#     try:
#         obj = model.objects.get(pk=id)
#         obj.delete()
#         return JsonResponse({'message': 'Successfully Deleted'})
#     except model.DoesNotExist:
#         return JsonResponse({'error': 'Item not found'}, status=404)


@login_required(login_url='/auth/login')
def Delete_image(request, id, column_name, model):
    prev_url= request.META.get('HTTP_REFERER', None)
    model=globals()[model]
    obj=get_object_or_404(model, pk=id)
    filepath=getattr(obj,column_name)
    filepath=filepath.path
    if filepath and os.path.isfile(filepath):
        os.remove(filepath)
        obj.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect(prev_url)
    messages.error(request, 'Image not deleted')
    return redirect(prev_url)

@login_required(login_url='/auth/login')
def Approve(request, id, model):
    prev_url= request.META.get('HTTP_REFERER', None)
    destination_model=globals()[model+'approved']
    model=globals()[model]
    source_instance=model.objects.get(pk=id)
    move_to_approved_data(request=request, source_instance=source_instance, destination_model=destination_model)
    return redirect(prev_url)

def move_to_approved_data(request,source_instance, destination_model):
    field_values={field.name: getattr(source_instance, field.name) for field in source_instance._meta.fields}
    aproved_data=destination_model(**field_values)
    aproved_data.save()
    source_instance.delete()
    return messages.success(request, 'Saved Successfully')

#project

@login_required(login_url='/auth/login')
def Data_Views(request,dir, template, model):
    model_saver=model
    model=globals()[model]
    approved_model=model_saver+'approved'
    approved_model=globals()[approved_model]
    template='staff/'+ dir +'/'+template+'.html'
    obj=model.objects.all()
    obj_appr=approved_model.objects.all()
    model=model_saver
    approved_model=model_saver+'approved'
    model={'model': model}
    appr_model={'model':approved_model}
    context={
        'obj':obj,
        'model':model,
        'appr_obj': obj_appr,
        'appr_model':appr_model
    }
    return render(request, template, context)



#customize

@login_required(login_url='/auth/login')
def Customize(request):
    
    context={

    'corousel_images':list(Corousel_Images.objects.values_list('corousel_images',  flat=True)),
    'outlook_images':list(Outlook_Images.objects.values_list('outlook_images', flat=True)),
    'team_images':list(Team_Images.objects.values_list('team_images', flat=True)),
    'projects_images':list(Upcoming_Project_Images.objects.values_list('Upcoming_Project', flat=True)),
    'events_images':list(Event_Images.objects.values_list('events_images', flat=True))
    }
    return render(request, 'staff/customize/customize.html', context)

@login_required(login_url='/auth/login')
def image_Project(request):  
    context={ 
    'upcoming_images':list(Upcoming_Project_Images.objects.values_list('Upcoming_Project', flat=True)),
    'ongoing_projects':list(Ongoing_Project_Images.objects.values_list('Ongoing_Project', flat=True)),
    'past_projects':list(Past_Project_Images.objects.values_list('Past_Project', flat=True)),
    }
    return render(request, 'staff/customize/project_images.html', context)

@login_required(login_url='/auth/login')
def Images_Edit(request, column_name, model):
    model_save=model
    model_form=globals()[model+'_Form']
    model=globals()[model]
    template='staff/customize/'+column_name+'.html'
    objs=model.objects.all()
    ids=[obj.pk for obj in objs ]
    objs=zip(objs,ids)
    context={
        'form':model_form,  
        'images':objs,
       
        
    }
    if request.method== 'POST':
        form=model_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image Added Successfully')
            return redirect('images',column_name=column_name, model=model_save)
        else:
            error=str(form.errors)
            messages.error(request, error)
            return render(request, template, context)
    return render(request, template, context)
  

@login_required(login_url='/auth/login')
def Busry_Data(request):
    context={
        
            'busary_images':list(Busary_Images.objects.values_list('busary_images',  flat=True)),
            'high_school_approved':Busaryapproved.objects.filter(education_level='High School').values_list('date', 'name', 'parent_name','phone_number','school_name', 'gender','ward', 'amount', 'id',),           
            'high_school':Busary.objects.filter(education_level='High School').values_list('date', 'name', 'parent_name','phone_number','school_name', 'gender','ward', 'amount', 'id',),         
            
            'collage_approved':Busaryapproved.objects.filter(education_level='Collage').values_list('date', 'name', 'parent_name','phone_number','school_name', 'gender','ward', 'amount', 'id',),           
            'collage':Busary.objects.filter(education_level='Collage').values_list('date', 'name', 'parent_name','phone_number','school_name', 'gender','ward', 'amount', 'id',),         
        
            'university_approved':Busaryapproved.objects.filter(education_level='University').values_list('date', 'name', 'parent_name','phone_number','school_name', 'gender','ward', 'amount', 'id',),           
            'university':Busary.objects.filter(education_level='University').values_list('date', 'name', 'parent_name','phone_number','school_name', 'gender','ward', 'amount', 'id',),         
     
           
            
            'form': Bus_Form(), 
            'busary':Busary.objects.all(),
            'appr_busary':Busaryapproved.objects.all(),
    }
    if request.method == 'POST':
        form = Bus_Form(request.POST)
        if form.is_valid():
            phone_Number=form.cleaned_data['phone_number']
            if Busary.objects.filter(phone_number=phone_Number).exists():
                messages.error(request, 'Already Applied')
                return render(request, 'staff/busary_data/busary_data.html', context)
            else:
                form.save()
                messages.success(request, 'Application saved successfully')
                return redirect('busary_data')  # Redirect to a success page or any other appropriate URL
        else:
            return render(request, 'staff/busary_data/busary_data.html', context)       
      # If it's a GET request or form is not valid
    return render(request, 'staff/busary_data/busary_data.html', context)
