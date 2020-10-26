from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    email = models.EmailField(max_length=254,unique=True)
    address = models.CharField(max_length=40)
    pincode = models.IntegerField()
    mobile = models.CharField(max_length=20,null=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name

class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    tracking_id = models.CharField(max_length=256,default=None)
    transaction_id = models.CharField(max_length=50,null=False)
    status=models.CharField(max_length=50,null=True,choices=STATUS)

class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=254,unique=True)
    address = models.CharField(max_length=254)
    pincode = models.IntegerField()

    def __str__(self):
        return self.name +" "+ self.email

class Product(models.Model):
    FABRIC = (
        ('Cotton','Cotton'),
        ('Silk','Silk'),
        ('Chiffon','Chiffon'),
        ('Woolen','Woolen'),
        ('Viscos','Viscos'),
        ('Rayon','Rayon'),
        ('Georegette','Georegette'),
        ('Synthetic','Synthetic')
    )
    CATEGORY = (
        ('Indian & Fusion Wear','Indian & Fusion Wear'),
        ('Western Wear', 'Western Wear'),
        ('Jewellery', 'Jewellery'),
        ('Accessories', 'Accessories'),
    )
    SUB_CATEGORY = (
        ("Kurtis, Tunics & Tops","Kurtis, Tunics & Tops"),
        ('Sarees','Sarees'),
        ('Skirts & Palazzos','Skirts & Palazzos'),
        ('Ethnic Dresses','Ethnic Dresses'),
        ('Lehenga Cholis','Lehenga Cholis'),
        ('Dupattas & Shawls','Dupattas & Shawls'),
        ('Dresses','Dresses'),
        ('Jumpsuits','Jumpsuits'),
        ('Tops, T-Shirts & Shirts','Tops, T-Shirts & Shirts'),
        ('Jeans & Jeggings','Jeans & Jeggings'),
        ('Trousers & Capris','Trousers & Capris'),
        ('Shorts & Skirts','Shorts & Skirts'),
        ('Shrugs','Shrugs'),
        ('Sweaters & Sweatshirts','Sweaters & Sweatshirts'),
        ('Jackets & Coats','Jackets & Coats'),
        ('Blazers & Waistcoats','Blazers & Waistcoats'),
        ('Leggings, Salwars & Churidars','Leggings, Salwars & Churidars'),
        ('Ponchoo','Ponchoo'),
    )
    SIZES = (
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('Plus Size','Plus Size')
    )
    seller = models.ForeignKey(Seller, verbose_name='seller_id', on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=450)
    product_category = models.CharField(max_length=50,null=True,choices=CATEGORY)
    sub_category = models.CharField(max_length=50,null=True,choices=SUB_CATEGORY)
    size = models.CharField(max_length=20,null=True,choices=SIZES)
    fabric = models.CharField(max_length=20,null=True,choices=FABRIC)
    quantity = models.IntegerField(default=1)
    brand = models.CharField(max_length =256,default=None)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name