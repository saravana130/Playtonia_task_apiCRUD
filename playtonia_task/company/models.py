from django.db import models
from django.core.validators import RegexValidator

contact_regex = RegexValidator(regex=r'^\d{10,10}$',
                               message="contact number must be entered in the format: '9999999999'. must be 10 digits allowed.")
# Create your models here.
class company(models.Model):
    name=models.CharField(max_length=50)
    contact_no = models.CharField(validators=[contact_regex],max_length=10)
    address=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class employees(models.Model):
    companyName=models.ForeignKey(company,on_delete=models.CASCADE)
    Fname=models.CharField(max_length=50)
    Lname=models.CharField(max_length=50)
    salary=models.PositiveIntegerField()
    contact_no=models.CharField(validators=[contact_regex],max_length=10)
    address=models.CharField(max_length=250)

    def __str__(self):
        name = str(self.Fname+" "+self.Lname)
        return name