from django.urls import path
from . import views
urlpatterns = [
    path('', views.proffessionals,
          name='proffessionals'),
    path('rejister/', views.prof_rejister,
          name='prof_rejister'),
]