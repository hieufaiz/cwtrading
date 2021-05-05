from django.urls import path, include
from . import views
app_name = 'appcovercall'
urlpatterns = [
    path('home/<str:symbol>', views.index, name='home'),
    path('saveCoverCall/', views.save_covercall, name='saveCoverCall'),
    path('showSymbol/', views.show_symbol, name='showSymbol'),
    path('backtestting/', views.backtest, name='backtestting'),
    path('backtestdemo/', views.estimate, name='backtestdemo')
]