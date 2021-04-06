from django import forms

class Covercallstrate(forms.Form):
    assetPrice = forms.FloatField()
    strikePrice = forms.FloatField()
    maturity = forms.FloatField()
    rate = forms.FloatField()
    startDate = forms.DateField()
    endDate = forms.DateField()
    symbol = forms.CharField()
class Closeprice(forms.Form):
    date = forms.DateField()
    symbol = forms.CharField()
    closePrice = forms.FloatField()