from django.shortcuts import render
from django.http import HttpResponse
from .forms import Covercall
from .models import CoverCall
import numpy as np
# Create your views here.
def index(request):
    covercall = Covercall
    a = np.array([1, 2])
    return render(request, 'covercall/index.html', {'covercall': covercall, 'a': a})

def save_covercall(request):
    if request.method == "POST":
        data = Covercall(request.POST)
        if data.is_valid():
            covercall = CoverCall(assetPrice = data.cleaned_data['assetPrice'],
                strikePrice = data.cleaned_data['strikePrice'],
                maturity = data.cleaned_data['maturity'],
                rate = data.cleaned_data['rate'],
                volatility = data.cleaned_data['volatility'],
                optionsPrice = data.cleaned_data['optionsPrice'],
                numberStock = data.cleaned_data['numberStock'],
                numberOption = data.cleaned_data['numberOption']) 
            covercall.save()
            return HttpResponse('save successful')
        else:
            return HttpResponse('Bad Request')

