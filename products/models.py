from django.db import models

# Create your models here.
class Product(models.Model):  
    name_product = models.CharField(max_length=255)  
    product_price = models.DecimalField(max_digits=10, decimal_places=2)  
    create_at = models.DateTimeField(auto_now_add=True)  
    update_at = models.DateTimeField(auto_now=True) 
    category_at=models.ManyToManyField('Category')  

    def __str__(self):  
        return f"Product Name: {self.name_product}, Price: {self.product_price} category:{self.category_at}"
    
class Category(models.Model):
    name_category=models.CharField(max_length=255)
    


    def __str__(self):
        return f"category:{self.name_category}"
