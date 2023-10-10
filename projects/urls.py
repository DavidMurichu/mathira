from django.urls import path
from . import views
urlpatterns = [
   
    path('<str:column_name>', views.project_view,
          name='project'),
    
    
    
    path('request_project/', views.request_project,
          name='request_project'),   
]