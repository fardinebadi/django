from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=254)
    phone_number=models.CharField(max_length=11,validators=[MinLengthValidator(11)])

    def __str__(self):
        return f"user name: {self.user_name} email:{self.email}  phone number:{self.phone_number} "