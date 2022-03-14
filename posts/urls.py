from django.urls import path
from django.urls import include
from . import views
from posts.api.router import router_posts

urlpatterns = [
    
    # Paths del Posts
    path('',include(router_posts.urls)),
]