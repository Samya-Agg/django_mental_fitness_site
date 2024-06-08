from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    description=models.TextField(max_length=500)
    age=models.IntegerField()
    playlist=models.TextField(max_length=200)
    contact=models.IntegerField()
    
class chat(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message=models.TextField(max_length=500)
    time=models.DateTimeField(auto_now=True)