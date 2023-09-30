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
    description = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    amount = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class History(models.Model): 
    STATUS = (
        ('Borrowed','Borrowed'),
        ('Returned','Returned')
    )
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)
    