from django.shortcuts import render
from staff.models import Event_Images,Corousel_Images

# Create your views here.
def Events(request, event_type):
    context={
    'corousel_images':list(Corousel_Images.objects.values_list('corousel_images',  'corousel_type')),
    'images':Event_Images.objects.filter(event_type=event_type).values_list('events_images', flat=True),
    'event_type':event_type 
}
    return render(request, 'events/events.html', context)