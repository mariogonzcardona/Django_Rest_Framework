"""django_rest_framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Endpoint for swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de Django Rest Framework",
      default_version='v1',
      description="Documentacion de Django Rest Framework de Mario Gonzalez",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=[permissions.AllowAny],
)

# Endpoint for apps
urlpatterns = [
    
    # Paths del Core
    path('',include('core.urls')),
    
    # Paths de Posts
    path('api/',include('posts.urls')),
    
    # Paths de Categories
    path('api/',include('categories.urls')),
    
    # Paths de Comments
    path('api/',include('comments.urls')),
    
    # Paths de User
    path('api/',include('user.urls')),
    
    # Paths de Admin de Django
    path('admin/', admin.site.urls),
    
    # Paths de Swagger
    # path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
