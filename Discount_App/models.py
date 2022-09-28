from email.policy import default
from nntplib import NNTPPermanentError
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date,datetime
from dateutil import parser
import os


####### Discount Model ########
class Discount(models.Model):
    DISCOUNT_TYPE = (
        ('FLAT', 'FLAT'),
        ('PERCENT', 'Percentage'),
    )

    DISCOUNT_CHOICES = (
        ('DATE', 'DATEWISE'),
        ('TIME', 'TIMEWISE'),
    )
    name = models.CharField(max_length=100,default="Discount")
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPE,blank = False,null = False)
    discount_amount = models.IntegerField(null=True,default = 0)

    discount_percentage = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(99)],null=True,default = 0)
    start_time = models.TimeField(default=datetime.now())
    end_time = models.TimeField(default=datetime.now())

    discount_category = models.CharField(max_length=10, choices=DISCOUNT_CHOICES,blank = False,null = False)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)

    Is_Valid   = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.discount_type=="FLAT":
            self.discount_percentage = 0
        else:
            self.discount_amount = 0

        if self.discount_category =="DATE":
            self.start_time= datetime.now().replace(hour=00, minute=0, second=0, microsecond=0)
            self.end_time= datetime.now().replace(hour=00, minute=0, second=0, microsecond=0)
            if self.end_date<date.today():
                self.Is_Valid = False
        else:
            self.start_date = date.today().replace(year=1000, month=1, day=2)
            self.end_date = date.today().replace(year=1000, month=1, day=2)
            if parser.parse(str(self.end_time)) < datetime.now():
                self.Is_Valid = False

        super(Discount, self).save(*args, **kwargs)







####### Category Model ########
class Category(models.Model):
    category_name = models.CharField(max_length=10,blank = False,null = False)


####### Product Model ########
class Product(models.Model):
    name = models.CharField(max_length=10,blank = False,null = False)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE) 
