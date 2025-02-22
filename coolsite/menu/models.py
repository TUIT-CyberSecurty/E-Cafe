from django.db import models

# Create your models here.
class Menu(models.Model):
    category = models.CharField(max_length=255)
    def __str__(self):
        return self.category

class food(models.Model):
    name = models.CharField(max_length= 255)
    description = models.TextField()
    cost = models.IntegerField()
    def __str__(self):
        return self.name
    