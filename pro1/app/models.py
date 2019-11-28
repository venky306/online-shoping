from django.db import models

class MerchantMdel(models.Model):
    indo=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    contact=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)

class ProductModel(models.Model):
    product_no=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_qty=models.IntegerField()
    merchant_id=models.ForeignKey(MerchantMdel,on_delete=models.CASCADE)