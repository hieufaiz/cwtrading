from django.urls import path, include
from . import views
app_name = 'appcovercallbacktest'
urlpatterns = [
    path('backtesting/', views.index, name='backtesting'),
]