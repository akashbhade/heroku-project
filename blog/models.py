from django.db import models

# Create your models here.

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    short_desc = models.CharField(max_length=500, default="")
    author = models.CharField(max_length=50, default="")
    slug = models.SlugField(max_length=200)
    time = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="blog/images")

    def __str__(self):
        return self.title

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    desc = models.TextField()
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fname
    