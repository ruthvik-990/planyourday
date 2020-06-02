from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name

# class Middle(models.Model):
#     profile=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)  

#     def __str__(self):
#         return self.profile.name      
class Task(models.Model):
    profile=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    # middle=models.ForeignKey(Middle,null=True,blank=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=200)
    status=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    class Meta:
        db_table='Task'    