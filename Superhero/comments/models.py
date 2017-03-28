from django.db import models

# Create your models here.

class comBatman(models.Model):
    comment = models.CharField(max_length=90,)
    author = models.CharField(max_length=25,)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author)
    
class comSuperman(models.Model):
    comment = models.CharField(max_length=90,)
    author = models.CharField(max_length=25,)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author)    
    
class comWonderWoman(models.Model):
    comment = models.CharField(max_length=90,)
    author = models.CharField(max_length=25,) 
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author)    
    