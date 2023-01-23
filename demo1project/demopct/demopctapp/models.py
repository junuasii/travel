from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    imge=models.ImageField(upload_to='pi')
    discription=models.TextField()

    def __str__(self):
        return self.name


class Member(models.Model):
    nam=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    dis=models.TextField()

    def __str__(self):
        return self.nam