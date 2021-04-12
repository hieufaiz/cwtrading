from django.db import models
from django.db.models import Model
# Create your models here.
class CoverCallStrate(models.Model):
    assetPrice = models.FloatField(null=True)
    strikePrice = models.FloatField(null=True)
    maturity = models.FloatField(null=True)
    rate = models.FloatField(null=True)
    startDate = models.DateField()
    endDate = models.DateField()
    symbol = models.CharField(max_length=10)
class ClosePrice(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=10)
    closePrice = models.FloatField(null=True)

class CWPrice(models.Model):
    dateCW = models.DateField()
    symbolCW = models.CharField(max_length=10)
    openPriceCW = models.FloatField(null=True)
    highPriceCW = models.FloatField(null=True)
    lowPriceCW = models.FloatField(null=True)
    closePriceCW = models.FloatField(null=True)
    volumeCW = models.FloatField(null=True)
    valueCW = models.FloatField(null=True)