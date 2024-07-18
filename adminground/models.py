from django.db import models

# Create your models here.
class Slider(models.Model):
    header = models.CharField(max_length=100)
    sub_header = models.CharField(max_length=100)
    image_path = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    def __str__(self):
        return f"id = {self.id} - {self.header} - {self.sub_header} - {self.image_path} - {self.active}"
    
class ServiceList(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=255)
    service_type = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    def __str__(self):
        return f"is_active => {self.active}  || id{self.id} subtitle =>({self.sub_title} serivce_type =>({self.service_type}))"
    
class Saurav(models.Model):
     name = models.CharField(max_length=50)
     def __str__(self):
        return f"|| id{self.id} name=> {self.name} "
     
class Surname(models.Model):
    surname = models.CharField(max_length=50)
    def __str__(self):
        return f"|| id{self.id} name=> {self.surname} "
    
class BlogList(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/images/')
    def __str__(self):
        return f"|| id{self.id} title=> {self.title} img=>{self.image}"