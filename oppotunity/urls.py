from django.urls import path
from . import views
urlpatterns = [
    path('', views.oppotunity,
          name='oppotunity'),
    path('oppotunity_sta/', views.oppotunity_sta,
          name='oppotunity_sta'),
]