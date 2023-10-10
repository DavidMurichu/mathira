from django.urls import path
from . import views
urlpatterns = [
    path('<str:event_type>', views.Events,
          name='upcoming'),
  
]