from email.mime import image
from operator import le
from statistics import mode
from django.db import models
from django  import forms


class Quiz(models.Model):
    question = models.CharField(max_length=200)
    variant1 = models.CharField(max_length=100)
    variant2 = models.CharField(max_length=100)
    variant3 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    image = models.ImageField(upload_to="images/%Y/%m/%d/")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["name", "email", "age", "image"]