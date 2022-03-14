from django.urls import path
from django.urls import include
from categories.api.router import router_categories

urlpatterns = [
    
    # Paths del Categories
    path('',include(router_categories.urls)),
]