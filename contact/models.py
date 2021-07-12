from django.db import models
# from phone_field import PhoneField
# Create your models here.
class contact(models.Model):
    fName = models.CharField(max_length=50,blank=False)
    lName = models.CharField(max_length=50,blank=False)
    phone = models.IntegerField(blank = False)
    email = models.EmailField(max_length=150,blank=False)
    def __str__(self):
        return self.fName
    