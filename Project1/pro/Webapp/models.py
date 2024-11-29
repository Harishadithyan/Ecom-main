from django.db import models
from cloudinary.models import CloudinaryField

class photo(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name
    
class card(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    image=models.URLField()
    name=models.CharField( max_length=50)
    Des=models.CharField( max_length=200)
    Price=models.IntegerField()
    quantity_choices = [(i, str(i)) for i in range(1, 21)]  
    available_quantity = models.PositiveIntegerField(choices=quantity_choices, default=1)

    def __str__(self):
        return self.name
