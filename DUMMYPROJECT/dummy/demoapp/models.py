from django.db import models
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name
class team(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics1')
    desc=models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
