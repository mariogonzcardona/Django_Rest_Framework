from django.urls import path
from django.urls import include
from comments.api.router import router_comments

urlpatterns = [
    
    # Paths del Categories
    path('',include(router_comments.urls)),
]