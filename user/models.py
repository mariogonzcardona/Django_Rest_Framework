from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # Es necesario hacer esto para que el campo email sea obligatorio y unico.
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True,max_length=200)
    twitter = models.URLField(blank=True,max_length=200)
    facebook = models.URLField(blank=True,max_length=200)
    
    # Proceso para poder loguearse con el email y no con el username
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
