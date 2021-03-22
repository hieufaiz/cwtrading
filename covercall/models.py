from django.db import models
from django.db.models import Model
# Create your models here.
class CoverCall(models.Model):
    assetPrice = models.FloatField(null=True)
    strikePrice = models.FloatField(null=True)
    maturity = models.FloatField(null=True)
    rate = models.FloatField(null=True)
    volatility = models.FloatField(null=True)
    optionsPrice = models.FloatField(null=True)
    numberStock = models.IntegerField(null=True)
    numberOption = models.IntegerField(null=True)
class ClosePrice(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=10)
    closePrice = models.FloatField(null=True)