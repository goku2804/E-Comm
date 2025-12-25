from django.urls import path
from .views import checkout, order_success, my_orders, invoice

app_name = 'orders'

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('success/<int:order_id>/', order_success, name='order_success'),
    path('my/', my_orders, name='my_orders'),
    path('invoice/<int:order_id>/', invoice, name='invoice')


]
