from django.shortcuts import render
from django.http import HttpResponse
from .forms import Covercallstrate
from .models import CoverCallStrate
from .forms import Closeprice
from .models import ClosePrice
import numpy as np
import scipy.stats as si
import sympy as sy
from sympy.stats import Normal, cdf
from sympy import init_printing
import pandas as pd
from datetime import datetime, timedelta
init_printing()
# Create your views here.

def call_option_price(S, K, t, r, sigma):
    d1 = [np.log(S / K) + (r + ((sigma**2) / 2)) * t] / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    call_price = S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * t) *  si.norm.cdf(d2, 0.0, 1.0)
    return call_price, si.norm.cdf(d1, 0.0, 1.0)[0]

def put_option_price(S, K, t, r, sigma):
    d1 = [np.log(S / K) + (r + ((sigma**2) / 2)) * t] / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    put_price = K * np.exp(-r * t)*si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0)
    return put_price

def save_covercall(request):
    if request.method == "POST":
        data = Covercallstrate(request.POST)
        if data.is_valid():
            startDate = data.cleaned_data['startDate']
            endDate = data.cleaned_data['endDate']
            symbol = data.cleaned_data['symbol']
            covercall = CoverCallStrate(assetPrice = data.cleaned_data['assetPrice'],
                strikePrice = data.cleaned_data['strikePrice'],
                maturity = data.cleaned_data['maturity'],
                rate = data.cleaned_data['rate'],
                startDate = data.cleaned_data['startDate'],
                endDate = data.cleaned_data['endDate'],
                symbol = data.cleaned_data['symbol'])
            covercall.save()
            volatility = get_volatility(startDate, endDate, symbol)
            call, deltaOptions = call_option_price(data.cleaned_data['assetPrice'], data.cleaned_data['strikePrice'],
                data.cleaned_data['maturity'], data.cleaned_data['rate'], volatility)
            put = put_option_price(data.cleaned_data['assetPrice'], data.cleaned_data['strikePrice'],
                data.cleaned_data['maturity'], data.cleaned_data['rate'], volatility)
            return render(request, 'covercall/campaign.html', {'assetPrice': data.cleaned_data['assetPrice'], 
                'strikePrice':  data.cleaned_data['strikePrice'], 
                'call': call[0], 'deltaOptions': deltaOptions, 'volatility': volatility, 'put': put[0] })
        else:
            return HttpResponse('Bad Request')

def show_symbol(request):
    symbols = ClosePrice.objects.values('symbol').distinct()
    return render(request, 'covercall/symbol.html', {'symbols': symbols})

def get_price(startDate, endDate, symbol):
    closeprice =  ClosePrice.objects.filter(symbol = symbol).values('closePrice')
    closeprice = closeprice.filter(date__gte = startDate, date__lte = endDate)
    arr_price = np.zeros(len(closeprice), )
    for index, price in enumerate(closeprice):
        arr_price[index] = price['closePrice']
    s_price = pd.Series(arr_price)
    return s_price

def calculate_volatility(data):
    logPrice = np.log(data / data.shift(1))
    daily_std =  np.std(logPrice)
    return daily_std.item() * 252 ** 0.5

def get_volatility(startDate, endDate, symbol):
    volatility = calculate_volatility(get_price(startDate, endDate, symbol))
    return volatility 

def index(request, symbol):
    covercall = Covercallstrate
    return render(request, 'covercall/index.html', {'covercall': covercall, 'symbol': symbol})
