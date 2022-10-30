from django.db import models
from django.apps import apps
from django.contrib.auth.models import User
from django.contrib.auth.models import User

# models import




# Create your models here.

class Rating(models.Model):
    # relationships
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    voter_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='voter')

    user_vote = models.IntegerField(default=0)
    comment = models.TextField(blank=True)

class Chat(models.Model):
    # Relationships
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    reciver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reciver")

    message = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)



class UserFavoriteAds(models.Model):
    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sell = models.ForeignKey('Sell', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username+" favourite "+self.product.name
# Create your models here.
class Category(models.Model):
    name =      models.CharField(max_length=50)
    parent =    models.ForeignKey('Category', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name =          models.CharField(max_length=50)
    category =      models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name

class SellImage(models.Model):
    # Relations
    sell =  models.ForeignKey('Sell', on_delete=models.CASCADE, related_name='sell_image') 
    url = models.ImageField(upload_to='product/static/product/images/% Y/% m/% d/', blank=True)

    def __str__(self):
        return "done"
        
class PurchaseImage(models.Model):
    # Relations
    purchase =  models.ForeignKey('Purchase', on_delete=models.CASCADE, related_name='purchase_image')
    url = models.ImageField(upload_to='product/static/product/images/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.purchase.description

class Address(models.Model):
    province =  models.CharField(max_length=20)
    district =  models.CharField(max_length=20)
    area =      models.CharField(max_length=40)
    
    def __str__(self):
        return self.area+" district #"+self.district+" "+self.province

class Purchase(models.Model):
    
    condition_choices = [
        ('used','used'),
        ('new', 'new'),
        ('like new', 'ln')
    ]

    # Relationship
    user =          models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_user')
    product =       models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchase_product')
    address =       models.ForeignKey(Address, on_delete=models.CASCADE, related_name='purchase_address')

    # Fields
    quantity =      models.IntegerField(null=True, blank=True)
    condition=      models.CharField(max_length=10, choices=condition_choices, null=True)
    description =   models.TextField(blank=True)
    price =         models.FloatField()
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)
    is_bought =     models.BooleanField(default=False)

    def __str__(self):
        return self.user.username+" purchase "+ str(self.id)

class Sell(models.Model):

    condition_choices = [
        ('used','used'),
        ('new', 'new'),
        ('like new', 'ln')
    ]

    price_type = [
        ('fixed','fixed'),
        ( 'negotiateble', 'vb'),
        ('give_away', 'To Give Away')
    ]

    # Relationship
    user =          models.ForeignKey(User, on_delete=models.CASCADE, related_name='sells_user')
    product =       models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sells_product')
    address =       models.ForeignKey(Address, on_delete=models.CASCADE, related_name='sells_address')

    # Fields
    quantity =      models.IntegerField(null=True, blank=True)
    condition=      models.CharField(max_length=10, choices=condition_choices, null=True)
    description =   models.TextField(blank=True)
    price =         models.FloatField()
    price_type =    models.CharField(max_length=20, choices=price_type, null=True)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)
    is_sold =       models.BooleanField(default=False)

    def __str__(self):
        return self.user.username+" sells "+str(self.id)    
    
    