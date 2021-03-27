from django.urls import path, include
from . import views
app_name = 'appcovercallbacktest'
urlpatterns = [
    path('backtesting/', views.index, name='backtesting'),
    path('backtesting_covercall/', views.backtesting_covercall, name='backtesting_covercall'),
]