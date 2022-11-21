from django.db import models
from django.utils import timezone


class Post(models.Model):
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    yaratilis_tarihi = models.DateTimeField(
            default=timezone.now)
    yayinlanma_tarihi = models.DateTimeField(
            blank=True, null=True)

    def yayinla(self):
        self. yayinlama_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik

class Personal(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    active_project = models.IntegerField()
    project_max = models.IntegerField()
    image = models.CharField(max_length=50)
    descripton = models.TextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title,'',self.__class__.__name__}"
   
class Professional(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    price = models.IntegerField()
    active_project = models.IntegerField()
    project_max = models.IntegerField()
    descripton = models.TextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title,'',self.__class__.__name__}"

class Business(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    price = models.IntegerField()
    active_project = models.IntegerField()
    project_max = models.IntegerField()
    descripton = models.TextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title,'',self.__class__.__name__}"
