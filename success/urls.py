
from django.contrib import admin
from django.urls import path, include
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('appointment/', include('appointment.urls')),
    path('busary/', include('busary.urls')),
    path('diaspora/', include('overseas.urls')),
    path('events/', include('events.urls')),
    path('proffessionals/', include('proffessionals.urls')),
    path('projects/', include('projects.urls')),
    path('oppotunities/', include('oppotunity.urls')),
    path('auth/', include('authentication.urls')),
    path('staff/', include('staff.urls')),
    
]
