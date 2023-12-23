from django.db import models

class Post(models.Model):
    ism = models.CharField(max_length=30)
    fam = models.CharField(max_length=30)
    yosh = models.CharField(max_length=2)
    adres = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)

    def __str__(self):
        return self.ism
