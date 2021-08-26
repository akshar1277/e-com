from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_data=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)




    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=90)
    car=models.CharField(max_length=200,default='')
    email = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
    city = models.CharField(max_length=90)
    state = models.CharField(max_length=90)
    zip_code = models.CharField(max_length=90)
    phone=models.CharField(max_length=10,default='')


class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default='')
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "....."