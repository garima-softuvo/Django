from email.policy import default
from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField(blank=True, null=False)
    summary     = models.TextField(blank=False, null=False)
    price       = models.DecimalField(decimal_places=2, max_digits=50)
    myfield     = models.CharField(max_length=120)
    featured    = models.BooleanField()   #null = True, default = Treu
    
