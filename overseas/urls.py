from django.urls import path
from . import views
urlpatterns = [
    path('rejister/', views.diaspora_register,
          name='diaspora_rejister'),
    path('', views.diaspora_affairs,
          name='diaspora'),
]