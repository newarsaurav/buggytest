from django.db import models

# Create your models here.
class Slider(models.Model):
    header = models.CharField(max_length=100)
    sub_header = models.CharField(max_length=100)
    image_path = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    def __str__(self):
        return f"id = {self.id} - {self.header} - {self.sub_header} - {self.image_path} - {self.active}"