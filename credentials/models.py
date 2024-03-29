from django.db import models
from django.urls import reverse


class Register(models.Model):
    username = models.CharField(max_length=250, default=True)
    password = models.TextField()
    conform_password = models.TextField()

    def __str__(self):
        return self.username


class Districts(models.Model):
    name = models.CharField(max_length=250)


    def __str__(self):
        return self.name



class Branch(models.Model):
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class AccountType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name





class FromTable(models.Model):
    name = models.CharField(max_length=50,blank=False)
    date_of_birth = models.DateField(null=True,blank=False)
    age = models.PositiveIntegerField(null=True,blank=False)
    phone_number = models.CharField(max_length=20,blank=False)
    mail_id = models.EmailField(max_length=254,unique=True,blank=False)
    address = models.TextField(blank=False)
    district = models.CharField(max_length=250,blank=False,default="thrissur")
    branch = models.CharField(max_length=250,blank=False,default='chalakudy')
    account_type = models.CharField(max_length=250,blank=True)
    choices = models.ManyToManyField('CheckboxOptions', blank=True)


    def __str__(self):
        return self.name


class CheckboxOptions(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class LoggedUser(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=75)

    def __str__(self):
        return self.name