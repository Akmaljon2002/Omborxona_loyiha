from django.contrib.auth.models import User
from django.db import models

class Ombor(models.Model):
    nom = models.CharField(max_length=50)
    tur = models.CharField(max_length=50, blank=True)
    manzil = models.CharField(max_length=50, blank=True)
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=14)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50, blank=True)
    miqdor = models.PositiveIntegerField()
    narx = models.PositiveIntegerField()
    olchov = models.CharField(max_length=20)
    kelgan_sana = models.DateTimeField(auto_now_add=True)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE, related_name='mahsulotlari')
    def __str__(self):
        return f"{self.nom} ({self.brend})"

class Client(models.Model):
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50, blank=True)
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=14)
    qarz = models.PositiveIntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE, related_name='clientlari')
    def __str__(self):
        return f"{self.ism} ({self.nom})"

