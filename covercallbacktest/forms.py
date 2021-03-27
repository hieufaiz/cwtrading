from django import forms

class Covercallbacktest(forms.Form):
    symbol = forms.CharField(max_length=10)
    startDate = forms.DateField()
    endDate = forms.DateField()
    callPrice = forms.FloatField()
    strikePrice = forms.FloatField()
