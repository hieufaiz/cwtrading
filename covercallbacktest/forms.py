from django import forms

class Covercallbacktest(forms.Form):
    symbol = forms.CharField()
    startDate = forms.DateField(input_formats=["%d-%m-%Y"])
    endDate = forms.DateField(input_formats=["%d-%m-%Y"])
    callPrice = forms.FloatField()
    strikePrice = forms.FloatField()
