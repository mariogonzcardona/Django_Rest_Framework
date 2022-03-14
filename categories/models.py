from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    published=models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True,default=None)
    # updated_at = models.DateTimeField(auto_now=True,default=None)
    
       #Metadata
    class Meta :
        verbose_name='categoria'
        verbose_name_plural='categorias'
        # ordering = ['-created_at']
    
    def __str__(self):
        return self.title