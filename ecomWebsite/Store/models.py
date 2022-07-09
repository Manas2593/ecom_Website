from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=1500)
    product_price = models.IntegerField()
    poduct_descp = models.CharField(max_length=15000)
    product_image_main = models.ImageField()
    brand_name= models.CharField(max_length=255)
    product_category = models.CharField(max_length=255)

    def __str__(self) -> None:
        return self.product_name



class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=255)


    
