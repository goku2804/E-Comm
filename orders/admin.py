
from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'is_paid')
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
