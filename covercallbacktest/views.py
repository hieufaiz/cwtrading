from django.shortcuts import render
from django.http import HttpResponse
from .forms import Covercallbacktest
from .models import CoverCallBacktest
from covercall.models import ClosePrice
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import statistics
def index(request):
    backtest = Covercallbacktest 
    # closeprice =  ClosePrice.objects.filter(symbol = 'FPT').values('closePrice')
    # closeprice = closeprice.filter(date__gte = "2014-01-15", date__lte = "2014-01-20")
    # arr_price = np.zeros(len(closeprice), )
    # for index, price in enumerate(closeprice):
    #     arr_price[index] = price['closePrice']
    # s_price = pd.Series(arr_price)
    # volatility = calculate_volatility(s_price)
    return render(request, 'covercallbacktest/index.html', {'backtest': backtest})

def calculate_volatility(data):
    logPrice = np.log(data / data.shift(1))
    daily_std = np.std(logPrice)
    return daily_std.item() * 252 ** 0.5

def get_price(startDate, endDate, symbol):
    closeprice =  ClosePrice.objects.values(symbol = symbol).values('closePrice')
    closeorice = closePrice.filter(date__gte = startDate, date__lte = endDate)
    arr_price = np.zeros(len(closeprice), )
    for index, price in enumerate(closeprice):
        arr_price[index] = price['closePrice']
    s_price = pd.Series(arr_price)
    return s_price

def get_volatility(startDate, endDate, symbol):
    # closeprice =  ClosePrice.objects.values(symbol = symbol).values('closePrice')
    # closeorice = closePrice.filter(date__gte = startDate, date__lte = endDate)
    # arr_price = np.zeros(len(closeprice), )
    # for index, price in enumerate(closeprice):
    #     arr_price[index] = price['closePrice']
    # s_price = pd.Series(arr_price)
    volatility = calculate_volatility(get_price(startDate, endDate, symbol))
    return volatility

def get_mean(startDate, endDate, symbol):
    return statistics.mean(get_price(startDate, endDate, symbol))

def get_max_min_price(startDate, endDate, symbol):
    closeprice =  ClosePrice.objects.values(symbol = symbol).values('closePrice')
    closeorice = closePrice.filter(date__gte = startDate, date__lte = endDate)
    arr_price = np.zeros(len(closeprice), )
    for index, price in enumerate(closeprice):
        arr_price[index] = price['closePrice']
    return np.amax(arr_price), np.amin(arr_price)

def get_log_returns(startDate, endDate, symbol):
    s_price = get_price(startDate, endDate, symbol)
    return (np.log(s_price) - np.log(s_price.shift(1))).tolist()

def portfolio_value(startDate, endDate, symbol, breakevenPoint, endPrice):
    # if endPrice - breakevenPoint > 0 :
    #     profit = endPrice - breakevenPoint
    #     return profit
    # else if endPrice - breakevenPoint < 0
    #     loss = breakevenPoint - endPrice
    #     return loss
    return 0
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
            volatility = get_volatility(startDate, endDate, symbol)
            breakevenPoint = callPrice + strikePrice
            sDate = datetime.strptime(startDate, "%m-%d-%Y")
            eDate = datetime.strptime(endDate, "%m-%d-%Y")
            deltaTime = str(eDate - sDate)
            maxPrice, minPrice = get_max_min_price(startDate, endDate, symbol) 
            strategy_backtester.save()
        else:
            return HttpResponse('Bad Request')