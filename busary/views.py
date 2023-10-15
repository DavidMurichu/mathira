from django.shortcuts import render, redirect
from .models import *
from staff.models import Busary_Images
from staff.models import Corousel_Images
from django.db.models import Count,Sum
import json


# Create your views here.
def busary(request):
    context={
    'corousel_images':list(Corousel_Images.objects.values_list('Corousel',  'corousel_type')),
    'images':list(Busary_Images.objects.values_list('Busary', flat=True))

    }
    return render(request, 'busary/busary_apply.html', context )

def busary_sta(request):
    count=Busary.objects.aggregate(name_count=Count('name'))
    count=count['name_count']
    approved=Busaryapproved.objects.aggregate(name_count=Count('name'))
    approved=approved['name_count']
    count=count +  approved
    if approved!=0:
        percentage= round( (approved/count)*100)
    else:
        percentage=0
    amount=Busaryapproved.objects.aggregate(amount=Sum('amount'))
    amount=amount['amount']
    pending=count-approved
    data={'count':count, 'amount':amount, 'approved':approved, 'pending':pending}
    data=json.dumps(data)
    context={
    'corousel_images':list(Corousel_Images.objects.values_list('Corousel',  'corousel_type')),
    'count':count,
    'amount':amount,
    'approved':approved,
    'percentage':percentage,
    'data':data
    }
    
    
    
    return render(request, 'busary/busary_sta.html', context)


     
