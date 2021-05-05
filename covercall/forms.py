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

class Cwprice(forms.Form):
    date = forms.DateField()
    symbol = forms.CharField()
    openPriceCW = forms.FloatField()
    highPriceCW = forms.FloatField()
    lowPriceCW = forms.FloatField()
    closePriceCW = forms.FloatField()
    volumeCW = forms.FloatField()
    valueCW = forms.FloatField()

class Covercallbt(forms.Form):
    startdateBt = forms.DateField()
    enddateBt = forms.DateField()
    timerange = forms.FloatField()
    c = forms.FloatField()
    m = forms.FloatField()
    n = forms.FloatField()

class Backtestcover(forms.Form):
    enddateBt = forms.DateField()
    timerange = forms.FloatField()
    rate = forms.FloatField()
    strikePrice = forms.FloatField()
    symbol = forms.CharField()
    maturity = forms.FloatField()

class Backtester(forms.Form):
    enddateBt = forms.DateField()
    timerange = forms.FloatField()
    m = forms.FloatField()
    n = forms.FloatField()
    symbol = forms.CharField()