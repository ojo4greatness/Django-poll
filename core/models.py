from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    quantity = models.IntegerField(blank=True, null=True)
    sku = models.IntegerField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)

def __str__(self):
    return self.name