from django.shortcuts import render
from django.http import HttpResponse
from .forms import Covercallbacktest
from .models import CoverCallBacktest
from covercall.models import ClosePrice
import numpy as np
import pandas as pd
import math
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
    closeprice =  ClosePrice.objects.filter(symbol = symbol).values('closePrice')
    closeorice = closeprice.filter(date__gte = startDate, date__lte = endDate)
    arr_price = np.zeros(len(closeprice), )
    for index, price in enumerate(closeprice):
        arr_price[index] = price['closePrice']
    s_price = pd.Series(arr_price)
    return s_price

def get_volatility(startDate, endDate, symbol):
    volatility = calculate_volatility(get_price(startDate, endDate, symbol))
    return volatility

def get_mean(startDate, endDate, symbol):
    return statistics.mean(get_price(startDate, endDate, symbol))

def get_max_min_price(startDate, endDate, symbol):
    closeprice =  ClosePrice.objects.filter(symbol = symbol).values('closePrice')
    closeorice = closeprice.filter(date__gte = startDate, date__lte = endDate)
    arr_price = np.zeros(len(closeprice), )
    for index, price in enumerate(closeprice):
        arr_price[index] = price['closePrice']
    return np.amax(arr_price), np.amin(arr_price)

def get_log_returns(startDate, endDate, symbol):
    s_price = get_price(startDate, endDate, symbol)
    return (np.log(s_price) - np.log(s_price.shift(1))).tolist()

def profit_loss(assetprice, breakevenPoint):
    if assetprice != breakevenPoint:
        return assetprice - breakevenPoint
    else:
        return 0

def portfolio_value(startDate, endDate, symbol, breakevenPoint):
    s_price = get_price(startDate, endDate, symbol)
    portfolio = np.zeros(len(s_price), )
    for index, price in enumerate(s_price):
        portfolio[index] = profit_loss(price, breakevenPoint)
    profit = np.zeros(len(portfolio), )
    loss = np.zeros(len(portfolio), )
    for i, price in enumerate(portfolio):
        if price > 0:
            profit[i] = price
        elif price < 0:
            loss[i] = price    
    return profit, loss

def backtesting_covercall(request):
    if request.method == "POST":
        data = Covercallbacktest(request.POST)
        #return render(request, 'covercallbacktest/backtest.html', {'data': data})
        if data.is_valid():
            symbol = data.cleaned_data['symbol']
            startDate = data.cleaned_data['startDate']
            endDate = data.cleaned_data['endDate']
            callPrice = data.cleaned_data['callPrice']
            strikePrice = data.cleaned_data['strikePrice']
            strategy_backtester = CoverCallBacktest(symbol = data.cleaned_data['symbol'], 
                startDate = data.cleaned_data['startDate'], 
                endDate = data.cleaned_data['endDate'], 
                callPrice = data.cleaned_data['callPrice'], 
                strikePrice = data.cleaned_data['strikePrice'])
            volatility = get_volatility(startDate, endDate, symbol)
            breakevenPoint = callPrice + strikePrice
            # sDate = datetime.strptime(startDate, "%d-%m-%Y")
            # eDate = datetime.strptime(endDate, "%d-%m-%Y")
            deltaTime = startDate - endDate
            maxPrice, minPrice = get_max_min_price(startDate, endDate, symbol)
            profit, loss = portfolio_value(startDate, endDate, symbol, breakevenPoint)
            maxProfit = np.amax(profit)
            maxLoss = np.amax(loss)
            if maxLoss < 0:
                maxLoss = maxLoss * -1
            minProfit = np.amin(profit)
            minLoss = np.amin(loss)
            if minLoss < 0:
                minLoss = minLoss * -1
            mean = get_mean(startDate, endDate, symbol)
            logReturn = get_log_returns(startDate, endDate, symbol)
            logReturn = [x for x in logReturn if math.isnan(x) == False]
            strategy_backtester.save()
            return render(request, 'covercallbacktest/backtest.html', {'breakevenPoint': breakevenPoint, 'startDate': startDate, 'endDate': endDate,
                'deltaTime': deltaTime, 'volatility': volatility, 'maxPrice': maxPrice, 'minPrice': minPrice, 'mean': mean, 'logReturn': max(logReturn),
                'maxProfit': maxProfit, 'minProfit': minProfit,'maxLoss': maxLoss, 'minLoss': minLoss })
        else:
            return HttpResponse('Bad Request')