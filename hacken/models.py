from django.db import models

# Create your models here.
class Hack(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hacken/images/',blank=True)
    file = models.FileField(upload_to='hacken/files/',blank=True)
    
    def __str__(self):
        return self.title
