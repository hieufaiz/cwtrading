from django.contrib import admin
from .models import CoverCall, ClosePrice

# Register your models here.
admin.site.register(CoverCall)
admin.site.register(ClosePrice)