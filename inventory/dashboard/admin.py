from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

admin.site.site_header = 'Inventário da ETEMAC'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'quantidade')
    list_filter = ['categoria']
    
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
# admin.site.unregister(Group)