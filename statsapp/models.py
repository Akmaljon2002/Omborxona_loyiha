from django.db import models
from asosiy.models import Mahsulot, Client

class Stats(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)
    miqdor = models.PositiveIntegerField()
    olchov = models.CharField(max_length=10, null=True, blank=True)
    summa = models.PositiveIntegerField()
    tolandi = models.PositiveIntegerField()
    qoldi = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.mahsulot} ({self.client})[{self.sana}]"
