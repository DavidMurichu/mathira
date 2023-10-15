from django.shortcuts import render, redirect, get_object_or_404
import os
from appointment.models import *
from overseas.models import *
from oppotunity.models import *
from proffessionals.models import *
from projects.models import *
from .models import *
from django.db.models import Count


from django.contrib.auth.decorators import login_required
from busary.models import *
from busary.forms import Bus_Form
from .forms import *
from django.contrib import messages




# Reused functions

#data query list with conditiion
def list_sort_return(model, column_name, creteria):
    model=model_generator(model=model)
    filter_params = {f'{column_name}__icontains': creteria}
    filtered_data = model.objects.filter(**filter_params).values_list()
    return filtered_data
# image model and model form Generator
def model_generator(model):
    return globals()[model]


# Saving File And Form Data
def form_file_save(request, model_form):
    form=model_form(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return messages.success(request, 'Event Successful')
    else:
        error=str(form.errors)
        return messages.error(request, error)
    
    
# Table Data Query
    
@login_required(login_url='/auth/login')
def Data_Views(request,dir, template, model):  
    template='staff/'+ dir +'/'+template+'.html'
    context=Parse_context_data_tables(model)
    return render(request, template, context)

# get data from database
def Parse_context_data_tables(model):
    model_saver=model
    model=model_generator(model=model)
    approved_model=model_saver+'approved'
    approved_model=model_generator(approved_model)
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
    return context

def staff_data_context(model):
    fields=['Outlook']
    model_approved=model+'approved'
    model=globals()[model]
    model_approved=globals()[model_approved]
    count=model.objects.aggregate(name_count=Count('date'))
    count=count['name_count']
    approved=model_approved.objects.aggregate(name_count=Count('date'))
    approved=approved['name_count']
    count=count+approved
    
    new=count-approved
    context={
        'applied':count,
        'approved':approved,
        'new':new
    }
    return context

@login_required(login_url='/auth/login')
def staff_page(request):
    model=['appointment','Busary', 'Proffession', 'oppotunities', 'diaspora']
    context={}
    for model in model:
        model_context=staff_data_context(model)
        context[model]=model_context
        
    context={
        'contexts':context
    }
    return render(request, 'staff/staff.html', context)


# Delete data from database

@login_required(login_url='/auth/login')
def Delete(request, id, model):
    prev_url= request.META.get('HTTP_REFERER', None)
    table_delete(request=request, model=model, id=id)
    return redirect(prev_url)

# Table Data delete function
def table_delete(request, model, id):
    model=model_generator(model=model)
    Object=model.objects.get(pk=id)
    Object.delete()
    return messages.success(request, 'Successfully Deleted')
   

# Deletion Batch Handler
@login_required(login_url='/auth/login')
def Delete_image(request, id, column_name):
    prev_url= request.META.get('HTTP_REFERER', None)
    delete_files(request=request, column_name=column_name, id=id)
    return redirect(prev_url)


# Delete files and table data
def delete_files(request, column_name, id):
    model=column_name+'_Images'
    model=model_generator(model=model)
    obj=get_object_or_404(model, pk=id)
    filepath=getattr(obj,column_name)
    filepath=filepath.path
    if filepath and os.path.isfile(filepath):
        os.remove(filepath)
        obj.delete()
        return messages.success(request, 'Successfully Deleted')    
    return messages.error(request, 'File not deleted')


    
    
    
# Approve Data Batch Handler
@login_required(login_url='/auth/login')
def Approve(request, id, model):
    prev_url= request.META.get('HTTP_REFERER', None)
    destination_model=model_generator(model=model+'approved')
    model=model_generator(model=model)
    source_instance=model.objects.get(pk=id)
    move_to_approved_data(request=request, source_instance=source_instance, destination_model=destination_model)
    return redirect(prev_url)

def move_to_approved_data(request,source_instance, destination_model):
    field_values={field.name: getattr(source_instance, field.name) for field in source_instance._meta.fields}
    aproved_data=destination_model(**field_values)
    aproved_data.save()
    source_instance.delete()
    return messages.success(request, 'Saved Successfully')






#customize

@login_required(login_url='/auth/login')
def Customize(request):
    
    context={

    'corousel_images':project_data('Corousel'),
    'outlook_images':project_data('Outlook'),
    'team_images':project_data('Team'),
    'projects_images':project_data('Project'),
    'events_images':project_data('Event')
    }
    return render(request, 'staff/customize/customize.html', context)



@login_required(login_url='/auth/login')
def image_Project(request):  

    context={ 
    'upcoming_images':Project_Images.objects.filter(project_type='Upcoming_Project').values_list('Project', flat=True),
    'ongoing_projects':Project_Images.objects.filter(project_type='Ongoing_Project').values_list('Project', flat=True),
    'past_projects':Project_Images.objects.filter(project_type='Past_Project').values_list('Project', flat=True),
    }
    return render(request, 'staff/customize/project_images.html', context)

def project_data(project_type):
    model=model_generator(model=project_type+'_Images')
    return list(model.objects.values_list(project_type, flat=True))

def dup_project_data(project_type):
    model=model_generator(model=project_type+'_Images')
    return list(model.objects.values_list(project_type, flat=True))


@login_required(login_url='/auth/login')
def Images_Edit(request, column_name):
    model=column_name+'_Images'
    model_form=globals()[model+'_Form']
    model=model_generator(model=model)
    template='staff/customize/'+column_name+'_images'+'.html'
    if request.method== 'POST':
        form_file_save(request, model_form)          
    objs=model.objects.all()
    ids=[obj.pk for obj in objs ]
    objs=zip(objs,ids)
    context={
        'form':model_form,  
        'images':objs,   
    }
    return render(request, template, context)
  


@login_required(login_url='/auth/login')
def Busry_Data(request):
    
    context={
        
            'busary_images':list(Busary_Images.objects.values_list('Busary',  flat=True)),
            'high_school_approved':list_sort_return(model='Busaryapproved', column_name='education_level',creteria='High School'),
            'high_school':list_sort_return(model='Busary', column_name='education_level', creteria='High School'),
            
            'collage_approved':list_sort_return(model='Busaryapproved', column_name='education_level',creteria='Collage'),
            'collage':list_sort_return(model='Busary', column_name='education_level', creteria='Collage'),
            
            'university_approved':list_sort_return(model='Busaryapproved', column_name='education_level',creteria='University'),
            'university':list_sort_return(model='Busary', column_name='education_level', creteria='University'),
            
            'form': Bus_Form(), 
           
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





@login_required(login_url='/auth/login')
def Event(request):  
    model_form=Event_Images_Form
    model='Event_Images'
    if request.method == 'POST':
        form_file_save(request, model_form)
        
    context={
        'upcoming':list_sort_return(model=model, column_name='event_type', creteria='Upcoming'),
        'past':list_sort_return(model=model, column_name='event_type', creteria='Past'),
        'form': model_form,  
                    
    } 
    return render(request, 'staff/customize/Event_images.html', context)
    

@login_required(login_url='/auth/login')
def project_staff(request, column_name):
    model=Project_Images
    model_form=Project_Images_Form
    if request.method == 'POST':
        form_file_save(request, model_form)
    context={
            'data':model.objects.filter(project_type=column_name).values_list(),
            'proj_type':column_name,
             'form': model_form,       
    } 
    template='staff/customize/project_staff.html'
    return render(request, template, context)


