from django.db import models
from User.models import regUser, userProfile

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(regUser, on_delete=models.CASCADE)#, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=1500, null=True)
    product_price = models.IntegerField(null=True)
    product_descp = models.CharField(max_length=15000, null=True)
    product_image_main = models.ImageField(null=True)
    brand_name= models.CharField(max_length=255, null=True)
    product_category = models.CharField(max_length=255, null=True)


    procuring_user = models.ForeignKey(userProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> None:
        return str(self.id)



class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=255)


    
