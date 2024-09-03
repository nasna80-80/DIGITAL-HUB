from django.db import models

class Login(models.Model):
    UserName=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)

class Company(models.Model):
    CompanyName=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    PhoneNumber=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Website=models.CharField(max_length=100)
    SocialMedia=models.CharField(max_length=100)
    AboutUs=models.CharField(max_length=100)
    ServiceOffered=models.CharField(max_length=100)
    Logo=models.CharField(max_length=100)

class Services(models.Model):
    Service=models.CharField(max_length=1000)
    Description=models.CharField(max_length=1000)
    Price=models.CharField(max_length=1000)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Gallery(models.Model):
    Image=models.CharField(max_length=100)
    Description=models.CharField(max_length=1000)


class Register(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    place=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)


class Request(models.Model):
    Date=models.DateField(max_length=100)
    Status=models.CharField(max_length=100)
    REGISTER=models.ForeignKey(Register,on_delete=models.CASCADE)
    SERVICES=models.ForeignKey(Services,on_delete=models.CASCADE)

class Complaint(models.Model):
    complaint=models.CharField(max_length=50)
    Reply=models.CharField(max_length=50)
    Status=models.CharField(max_length=50)
    Date=models.CharField(max_length=50)
    REGISTER = models.ForeignKey(Register, on_delete=models.CASCADE)

class payment(models.Model):
    Date=models.CharField(max_length=100)
    REGISTER = models.ForeignKey(Register, on_delete=models.CASCADE)
    SERVICES = models.ForeignKey(Services, on_delete=models.CASCADE)
    price=models.CharField(max_length=100)