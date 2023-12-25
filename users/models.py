from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField()
    description = models.CharField(max_length=100, default='Hello Everyone')
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    
    def __str__(self):
        return self.username
