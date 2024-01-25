from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=250)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name

class Branch(models.Model):
    name=models.CharField(max_length=250)
    district= models.CharField(max_length=250)

    def __str__(self):
        return self.name