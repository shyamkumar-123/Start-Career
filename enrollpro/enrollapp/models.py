from django.db import models
#import uuid
from django.contrib.auth.models import User


class Course(models.Model):
    DURATION=((12,'12 Months'),(6,'6 Months'),(4,"4 Months"))
    Course_name=models.CharField(max_length=100,default=True)
    image=models.ImageField(upload_to='images')
    duration=models.IntegerField(default=True,choices=DURATION)
    Hours=models.IntegerField(default=True)
    Fee=models.BigIntegerField(default=True)
    Details=models.TextField(max_length=800,default=True)

    def __str__(self):
        return self.Course_name
    

class Trainer(models.Model):
    EXP=((8,"8 Years"),(9,'9 Years'),(4,'4 Years'),(6,'6 Years'),(5,'5 Years'))
    name=models.CharField(max_length=40)
    languages=models.CharField(max_length=40)
    Experience=models.IntegerField(choices=EXP)
    
    def __str__(self):
        return self.name
    
'''class Cart(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    totalprice=models.FloatField(default=0.00)
    timestamp=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='cart'''




'''class cartItem(models.Model):
    Course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='items')
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cartitems")
    quantity=models.IntegerField(default=0)

    def __str__(self):
        return self.Course.Course_name
'''

class Payment(models.Model):
    payment_id=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id
        
class Order(models.Model):
    #Course_name=models.ManyToManyField(Course)
    #Fee=models.ManyToManyField(Course)
    orderId=models.CharField(max_length=10,unique=True)
    #date=models.DateTimeField()
    def __str__(self):
        return self.orderId
    



