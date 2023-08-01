from django.db import models

# Create your models here.
class info(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    mobile_no = models.CharField(max_length=150, null=True, blank=True)
    fr = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    to = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    room = models.CharField(max_length=50, null=True, blank=True)

    
    def __str__(self):
        return self.name