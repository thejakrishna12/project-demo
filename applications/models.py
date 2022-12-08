from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True, null=False)
    password = models.CharField(max_length=150)
    password2 = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username