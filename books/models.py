from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField('Published-Date', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Contact(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    message = models.TextField()





    def __str__(self):
        return self.name

class Forum(models.Model):
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=20,blank=True)
    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100,blank=True)
    zip = models.CharField(max_length=6, blank=True)
    check_me_out = models.BooleanField(default=False)

    def __str__(self):
        return self.email
