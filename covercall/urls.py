from django.urls import path, include
from . import views
app_name = 'appcovercall'
urlpatterns = [
    path('', views.index, name='home'),
    path('saveCoverCall/', views.save_covercall, name='saveCoverCall'),
]