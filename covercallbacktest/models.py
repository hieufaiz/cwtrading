from django.db import models
from django.db.models import Model
# Create your models here.
class CoverCallBacktest(models.Model):
    symbol = models.CharField(max_length=10)
    startDate = models.DateField()
    endDate = models.DateField()
    callPrice = models.FloatField(null=True)
    strikePrice = models.FloatField(null=True)

