from django import forms

class Covercall(forms.Form):
    assetPrice = forms.FloatField()
    strikePrice = forms.FloatField()
    maturity = forms.FloatField()
    rate = forms.FloatField()
    volatility = forms.FloatField()

class Closeprice(forms.Form):
    date = forms.DateField()
    symbol = forms.CharField()
    closePrice = forms.FloatField()