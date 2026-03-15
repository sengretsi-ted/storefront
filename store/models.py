from django.db import models

# Create your models here.

# Promotion - Product (Many to Many)
class Promotion(models.Model):
    description = models.CharField(max_length=255) #varchar(255)
    discount = models.FloatField() #float
    

class Collection(models.Model):
    title = models.CharField(max_length=255) #varchar(255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+') #foreign key to Product, with set null on delete, and no reverse relation
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['title'] #ordering by title in ascending order, use '-title' for descending order


class Product(models.Model):
    title = models.CharField(max_length=255) #varchar(255)
    slug = models.SlugField()
    description = models.TextField() #text
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) #decimal(10,2)  # 9999.99 as a sample number
    inventory = models.IntegerField() #int
    last_update = models.DateTimeField(auto_now=True) #datetime
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT) #foreign key to Collection, with protect delete so a deleted collection will not delete the products in it, but will raise an error instead
    promotions = models.ManyToManyField(Promotion) #many to many relationship with Promotion

    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['title'] #ordering by title in ascending order, use '-title' for descending order

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]

    first_name = models.CharField(max_length=255) #varchar(255)
    last_name = models.CharField(max_length=255) #varchar(255)
    email = models.EmailField(unique=True) #varchar(254)
    phone = models.CharField(max_length=20) #varchar(20)
    birth_date = models.DateField(null=True) #date
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE) #char(1)
    

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True) #datetime
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING) #varchar(20)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT) #foreign key to Customer, with cascade delete


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT) #foreign key to Order, with cascade delete
    product = models.ForeignKey(Product, on_delete=models.PROTECT) #foreign key to Product, with cascade delete
    quantity = models.PositiveSmallIntegerField() #positive integer
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) #decimal(6,2)
    
    

class Address(models.Model):
    street = models.CharField(max_length=255) #varchar(255)
    city = models.CharField(max_length=255) #varchar(255)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE) #foreign key to Customer, with cascade delete
    zip_code = models.CharField(max_length=20, null=True)



class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) #datetime

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) #foreign key to Cart, with cascade delete
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #foreign key to Product, with cascade delete
    quantity = models.PositiveSmallIntegerField() #positive integer
































