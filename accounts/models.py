from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    STATUS = (
        ('Available', 'Available'),
        ('Empty', 'Empty'),
    )
    name = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    amount = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
class History(models.Model): 
    STATUS = (
        ('Borrowed','Borrowed'),
        ('Returned','Returned')
    )
    #staff =
    #item =
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)
    