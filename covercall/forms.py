from django import forms

class Covercall(forms.Form):
    assetPrice = forms.FloatField()
    strikePrice = forms.FloatField()
    maturity = forms.FloatField()
    rate = forms.FloatField()
    volatility = forms.FloatField()
    optionsPrice = forms.FloatField()
    numberStock = forms.IntegerField()
    numberOption = forms.IntegerField()