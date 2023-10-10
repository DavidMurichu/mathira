from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.busary,
          name='busary'),
    path('statistics/', views.busary_sta,
          name='busary_sta'),
   
    

]