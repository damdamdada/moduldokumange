from django.db import models

class Work (models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='workshop/images', blank=True)
    file = models.FileField(upload_to='workshop/files', blank=True)
    
    def __str__(self):
        return self.title
