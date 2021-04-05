from django.db import models

# Create your models here.
class Shop(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='sondershop/images',blank=True)
    file = models.FileField(upload_to='sondershop/files',blank=True)
    
    def __str__(self):
        return self.title
