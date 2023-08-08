#accessing a user model for registration of the user in django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
# Create your models here.

#defining a table called category
# class UserProfile(AbstractUser):
#     username = models.CharField(max_length=100,unique=True,)
#     email = models.CharField(unique=True)
#     phone = models.CharField(blank=True)
    
#     def __str__(self):
#         return self.username
#     class Meta:
#         db_table = 'spare_users'
#         verbose_name = 'user'
#         verbose_name_plural = 'users'
        
class Category(models.Model):
    name = models.CharField(max_length=50, null= False, blank= False, unique=True)
    #this described how the class category will be required by other classes
    def __str__(self):
        return self.name
    
#defining a table called product
class Product(models.Model):
    #referencing the category of the product
    Category_name = models.ForeignKey(Category, on_delete= models.CASCADE, null=False, blank= False)
    #reserved for the date of arrival
    item_name = models.CharField(max_length=50, null= False, blank= False)
    total_quantity = models.IntegerField(default= 0, null=False, blank=False, validators=[MinValueValidator(1)])
    issued_quantity = models.IntegerField(default= 0, null=False, blank=False)
    received_quantity = models.IntegerField(default= 0, null=False, blank=False)
    unit_price = models.IntegerField(default= 0, null=False, blank=False)
    
    def __str__(self):
        return self.item_name

class Sale(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(default=0, null=False, blank=False)
    amount_received = models.IntegerField(default=0, null=False, blank=False)
    issued_to = models.CharField(max_length=100, null=False, blank=False)
    unit_price = models.IntegerField(default=0, null=False, blank=False)
    
    #total sales
    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)
    
    #to get the change after payment
    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))
        #abs stands for absolute values 
    
    def __str__(self):
        return self.item.item_name