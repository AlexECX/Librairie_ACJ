from django.contrib import admin

# Register your models here.
from .models import Sale, History, SessionCart

admin.site.register(Sale)
admin.site.register(History)
admin.site.register(SessionCart)