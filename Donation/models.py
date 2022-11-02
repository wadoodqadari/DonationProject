# Create your models here.
from email.policy import default
from django.db import models
# from user.models import Donar
# from django.contrib.auth.models import User
# from backend.models import Category 
# Create your models here.

# class Product(models.Model):
#     name=models.CharField(max_length=30)
#     # Category=models.ForeignKey(Category,on_delete=models.CASCADE)
#     # category = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
#     quantity=models.CharField(max_length=30,null=True)
#     # Donar_id=models.ForeignKey(Donar,on_delete=models.CASCADE,null=True)
#     receving_date=models.DateField

#     def __str__(self) :
#         return self.quantity ,self.Donar_id,self.receving_date

class Product (models.Model):
    name = models.CharField(max_length=30 )
    quantity = models.IntegerField(default=True)

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self) :
        return self.name

from django.db import models

# class Todo(models.Model):
#    title = models.CharField(max_length=100)
#    description = models.TextField()
#    completed = models.BooleanField(default=False)

#    def _str_(self):
#      return self.title



