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

class CoverCallBacktest(models.Model):
    startdateBt = models.DateField()
    enddateBt = models.DateField()
    timerange = models.FloatField(null=True)
    c = models.FloatField(null=True)
    m = models.FloatField(null=True)
    n = models.FloatField(null=True)

class BackTestCover(models.Model):
    enddateBt = models.DateField()
    timerange = models.FloatField(null=True)
    rate = models.FloatField(null=True)
    strikePrice = models.FloatField(null=True)
    symbol = models.CharField(max_length=10)
    maturity = models.FloatField(default=0.5)

class BackTester(models.Model):
    enddateBt = models.DateField()
    timerange = models.FloatField(null=True)
    m = models.FloatField(null=True)
    n = models.FloatField(null=True)
    symbol = models.CharField(max_length=10)