from django.shortcuts import render
from staff.models import Event_Images,Corousel_Images

# Create your views here.
def Events(request, event_type):
   

    context={
    'corousel_images':list(Corousel_Images.objects.values_list('Corousel',  'corousel_type')),
    'images':Event_Images.objects.filter(event_type=event_type).values_list('Event', 'event_name', 'event_agenda', 'event_date', 'event_place'),
    'event_type':event_type 
}
    return render(request, 'events/events.html', context)