from django import forms

from myapp.models import *


class AdminLoginForm(forms.Form):
    UserName= forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'USERNAME', 'class': 'form-control',}),
                           max_length=100)
    Password=forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'PASSWORD','class':'form-control'}),max_length=50)
    class Meta:
        model = Login
    def save(self):
        details = Login()
        details.name = self.data['UserName']
        details.place = self.data['Password']
        details.save()

class CompanyProfile(forms.Form):
    CompanyName = forms.CharField(label="Company name", widget=forms.TextInput(attrs={'placeholder': 'COMPANYNAME', 'class': 'forms-control','pattern':'[a-z A-Z]*'}),
                               max_length=100)
    Address = forms.CharField(label='Addres',widget=forms.Textarea(attrs={'placeholder': 'Address', 'class': 'forms-control','rows':4,'cols':40}),
                                  max_length=100)
    PhoneNumber = forms.CharField(label="phone number",required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number', 'class': 'forms-control','pattern':'[0-9]{3}-[0-9]{3}-[0-9]{4}'}),
                             max_length=100)
    Email=forms.EmailField(required=True,label="Email",widget=forms.EmailInput(attrs={'placeholder':'enter your email','pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$}'}),
                           max_length=100)
    Website=forms.CharField(label='Website',widget=forms.TextInput(attrs={'placeholder':'enter your company website','class':'forms-control'}),
                            max_length=120)
    SocialMedia=forms.CharField(label='Social Media',widget=forms.TextInput(attrs={'placeholder':'websites','class':'forms-control'}),
                                max_length=200)
    AboutUs=forms.CharField(label="AboutUs",widget=forms.Textarea(attrs={'placeholder':'about','class':'forms-control'}),
                           max_length=1000)
    SeviceOffered=forms.CharField(label='Services',widget=forms.Textarea(attrs={'placeholder':'services offerd','class':'forms-control'}),
                                 max_length=10000)
    Photo=forms.ImageField(required=True,label='upload photo',widget=forms.FileInput(attrs={'accept':'image/*'}))

class Service_form(forms.Form):
    Service=forms.CharField(label='services',widget=forms.TextInput(attrs={'class':'form-control'}),max_length=1000)
    Description=forms.CharField(label='Description',widget=forms.Textarea(attrs={ 'class': 'form-control','rows':4,'cols':40}),
                                  max_length=10000)
    Price=forms.CharField(label='price',widget=forms.Textarea(attrs={'class':'form-control','rows':4,'cols':40,'pattern':'^\d+(\.\d{1,2})?$'}),max_length=1000)


class Gallery_form(forms.Form):
    Images=forms.ImageField(required=True,label='Upload Image',widget=forms.FileInput(attrs={'accept':'image/*'}))
    Description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder': 'Description', 'class': 'forms-control', 'rows': 4, 'cols': 40}),
                                  max_length=100000)


class User_Register(forms.Form):
    Name=forms.CharField(required=True,label="name",widget=forms.TextInput(attrs={'placeholder':'name','class':'form-control','pattern':'[a-z A-Z]*'}),max_length=100 )
    Password=forms.CharField(required=True,label="password",widget=forms.TextInput(attrs={'placeholder':'password','class':'form-control','pattern':'(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}'}),max_length=100)
    Email=forms.CharField(required=True,label="Email",widget=forms.TextInput(attrs={'placeholder':'email','class':'form-control','pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$}'}),max_length=100)
    Place=forms.CharField(label="place",widget=forms.TextInput(attrs={'placeholder':'place','class':'form-control','pattern':''}),max_length=100)
    Phone=forms.CharField(required=True,label="phone",widget=forms.TextInput(attrs={'placeholder':'phone','class':'form-control','pattern':'[0-9]{3}-[0-9]{3}-[0-9]{4}'}),max_length=100)