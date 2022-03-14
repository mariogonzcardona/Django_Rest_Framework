from django.contrib import admin
from .models import Category

# Register your models here.
@admin.register(Category) # Esto es para registrar el modelo
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','published']
    
# El decorador reemplaza a admin.site.register(Category,CategoryAdmin)
# Por @admin.register(Category)