from . import views
from django.urls import path, include
 

urlpatterns = [
    path('', views.staff_page, name='staff' ),
    
    path('data/<str:dir>/<str:template>/<str:model>', views.Data_Views, name='data' ),
   
    path('busary_data/', views.Busry_Data,
          name='busary_data'),
    
    path('customize/', views.Customize,
        name='customize'),
    
    path('projects_customizer/', views.image_Project,
    name='project_customizer'),

    
    path('customizer/<str:column_name>/<str:model>', views.Images_Edit,
        name='images'),
   
   
    path('delete/<int:id>/<str:model>', views.Delete,
    name='delete'),
    
    # path('Delete/<int:id>/<str:model>', views.delete,
    # name='Delete'),
    
    path('approve/<int:id>/<str:model>', views.Approve,
    name='approve'),
    
    path('delete_image/<int:id>/<str:column_name>/<str:model>', views.Delete_image,
    name='delete_image'),

]