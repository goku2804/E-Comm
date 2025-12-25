from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib import messages
from cart.models import Cart, CartItem

def checkout(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    if not items.exists():
        messages.error(request, "Your cart is empty.")
        return redirect('cart:view_cart')

    order = Order.objects.create(user=request.user)

    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )

    items.delete()

    messages.success(request, "Order placed successfully!")
    return redirect('orders:order_success', order.id)



@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})




    return redirect('orders:order_success', order.id)
def order_success(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/success.html', {'order': order})

def invoice(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/invoice.html', {'order': order})
