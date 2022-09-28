from django.db import models

# Create your models here.
class Contact(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)
    phone=models.CharField(max_length=12)
    message=models.TextField(max_length=200)
    
    def __str__(self) :
        return "Name :- "+self.firstName+"  "+self.lastName+"               Email :-"+self.email+" Phone no :-"+self.phone
    
class Feedback(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=40)
    message=models.TextField(max_length=200)
    
    def __str__(self) :
        return "By "+self.name+"  : "+self.email+"    says :- "+self.message
    

class ProductDetails:
    desc : str
    img : str
    price : int
    link:str
    brand:str
    website:str
    originalPrice:str
    discount:str
    id:str

