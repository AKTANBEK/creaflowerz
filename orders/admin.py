from django.contrib import admin
from .models import Order, FlowerOrder, GoodsOrder


class FlowerOrderInline(admin.TabularInline):
    model = FlowerOrder
    raw_id_fields = ['flower']


class GoodsOrderInline(admin.TabularInline):
    model = GoodsOrder
    raw_id_fields = ['good']


@admin.register(FlowerOrder)
class FlowerOrderAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(GoodsOrder)
class GoodsOrderAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['payment_method', 'delivery_method', 'gift',
                    'phone', 'delivery_date', 'created_date',
                    'address', 'paid']
    inlines = [FlowerOrderInline, GoodsOrderInline]