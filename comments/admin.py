from django.contrib import admin
from .models import Comment

# Register your models here.
@admin.register(Comment) # Esto es para registrar el modelo
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'post', 'created_at' )
    
# El decorador reemplaza a admin.site.register(Comment,CommentAdmin)
# Por @admin.register(Comment)