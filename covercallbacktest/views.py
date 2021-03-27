from django.shortcuts import render
from django.http import HttpResponse
from .forms import Covercallbacktest
from .models import CoverCallBacktest
from covercall.models import ClosePrice
import numpy as np
def index(request):
    backtest = Covercallbacktest 
    closeprice = ClosePrice.objects.all()
    return render(request, 'covercallbacktest/index.html', {'backtest': backtest, 'closeprice': closeprice})
#def get_volatility(startDate, endDate):


def backtesting_covercall(request):
    if request.method == "POST":
        data = Covercallbacktest(request.POST)
        symbol = data.cleaned_data['symbol']
        startDate = data.cleaned_data['startDate']
        endDate = data.cleaned_data['endDate']
        callPrice = data.cleaned_data['callPrice']
        endPrice = data.cleaned_data['endPrice']
        strikePrice = data.cleaned_data['strikePrice']
        if data.is_valid():
            strategy_backtester = CoverCallBacktest(symbol, startDate, endDate, callPrice, endPrice, strikePrice)
            strategy_backtester.save()
        else:
            return HttpResponse('Bad Request')