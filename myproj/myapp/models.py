from django.db import models


class books(models.Model):
  name =  models.CharField(max_length=200)
  dob = models.DateField(auto_now=True)
  author = models.CharField(max_length=200)
  count =  models.IntegerField()
  price = models.ForeignKey("books_price", on_delete=models.CASCADE)

  
  

  def __str__(self):
    return self.name
  



class books_price(models.Model):
  price = models.IntegerField()

  def __str__(self):
    return str(self.price) + " Руб"





class books2(models.Model):
  name =  models.CharField(max_length=200)
  dob = models.DateField(auto_now=True)
  author = models.CharField(max_length=200)
  count =  models.IntegerField()
# Create your models here.



class Animal(models.Model):
  name = models.CharField(max_length= 100)
  voice = models.CharField(max_length= 100)

  def speak(self, a):
    return  a * 20 #f'The {self.name} says "{self.voice}"'
