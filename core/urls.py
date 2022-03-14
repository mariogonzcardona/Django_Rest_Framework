from django.urls import path
from . import views

urlpatterns = [
    
    # Paths del Core
    path('',views.home,name='home'),
]