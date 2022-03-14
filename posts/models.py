from django.db import models
from django.db.models import SET_NULL
from user.models import User
from categories.models import Category

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug=models.SlugField(max_length=255, unique=True)
    image=models.ImageField(upload_to='posts/images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category=models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    
    #Metadata
    class Meta :
        verbose_name='post'
        verbose_name_plural='posts'
        ordering = ['id']

    def __str__(self):
        return self.title
