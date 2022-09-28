from django.db import models
from django.contrib.auth.models import User
# from home.models import users
# Create your models here.
class product(models.Model):
    product_id=models.CharField(max_length=50)
    product_name=models.CharField(max_length=300,default='')
    link=models.URLField(max_length=500)
    curr_price=models.IntegerField()
    old_price=models.IntegerField()
    website=models.CharField(max_length=10)
    # user=models.ForeignKey(to="User")
    users=models.ManyToManyField(User)

    def __str__(self):
        return self.product_name
