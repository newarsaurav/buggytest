from django.db import models

# Create your models here.
    
class landing_banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255 ,default='Default description')
    image = models.ImageField(upload_to='static/forntpage/img/landing_banner')

    def __str__(self):
        return f"id({self.id} text=> {self.title})"

class banner(models.Model):
    icons = models.ImageField(upload_to='static/forntpage/img/banner_icons')
    text = models.CharField(max_length=255)
    def __str__(self):
        return f"id({self.id} text=> {self.text})"
    
class service_list(models.Model):
    
    image = models.ImageField(upload_to='static/forntpage/img/servicelist')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    def __str__(self) :
        return f"id({self.id} title=>{self.title})"

class why_buggy_cloud(models.Model):
    image = models.ImageField(upload_to='static/forntpage/img/whybuggy')
    title = models.CharField(max_length=100)
    description = models.TextField(default=' ')

    def __str__(self) :
        return f"id({self.id} title=>{self.title})"
    
class front_blog(models.Model):

    image = models.ImageField(upload_to='static/forntpage/img/whybuggy')
    subtitle = models.CharField(max_length=100 , default=' ')
    title = models.CharField(max_length=100)
    description = models.TextField(default=' ')

    def __str__(self) :
        return f"id({self.id} title=>{self.title})"