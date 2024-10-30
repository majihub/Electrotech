from django.contrib import admin

from eletrotechapp.models import Payment, Products

# Register your models here.
admin.site.register(Products)
admin.site.register(Payment)