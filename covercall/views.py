from django.shortcuts import render
from django.http import HttpResponse
from .forms import Covercall
from .models import CoverCall
import numpy as np
import scipy.stats as si
import sympy as sy
from sympy.stats import Normal, cdf
from sympy import init_printing
init_printing()
# Create your views here.
def index(request):
    covercall = Covercall
    a = np.array([1, 2])
    return render(request, 'covercall/index.html', {'covercall': covercall, 'a': a})

def call_option_price(S, K, t, r, sigma):
    d1 = [np.log(S / K) + (r + ((sigma**2) / 2)) * t] / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    call_price = S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * t) *  si.norm.cdf(d2, 0.0, 1.0)
    return call_price
def put_option_price(S, K, t, r, sigma):
    d1 = [np.log(S / K) + (r + ((sigma**2) / 2)) * t] / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    put_price = K * np.exp(-r * t)*si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0)
    return put_price
def save_covercall(request):
    if request.method == "POST":
        data = Covercall(request.POST)
        if data.is_valid():
            covercall = CoverCall(assetPrice = data.cleaned_data['assetPrice'],
                strikePrice = data.cleaned_data['strikePrice'],
                maturity = data.cleaned_data['maturity'],
                rate = data.cleaned_data['rate'],
                volatility = data.cleaned_data['volatility'])
            covercall.save()
            # call = mb.BS([ data.cleaned_data['assetPrice'], data.cleaned_data['strikePrice'],
            #     data.cleaned_data['rate'], data.cleaned_data['maturity'] ], data.cleaned_data['volatility']).callPrice
            call = call_option_price( data.cleaned_data['assetPrice'], data.cleaned_data['strikePrice'],
                data.cleaned_data['maturity'], data.cleaned_data['rate'], data.cleaned_data['volatility'])
            campaign = {'assetPrice': data.cleaned_data['assetPrice'], 
                'strikePrice':  data.cleaned_data['strikePrice'], 'call': call} 
            return render(request, 'covercall/campaign.html', {'assetPrice': data.cleaned_data['assetPrice'], 
                'strikePrice':  data.cleaned_data['strikePrice'], 'call': call[0] } )
        else:
            return HttpResponse('Bad Request')

