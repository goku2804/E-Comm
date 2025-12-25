from django.shortcuts import render, redirect
from .models import Cart, CartItem
from products.models import Product


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    cart, _ = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        item.quantity += 1
        item.save()

    return redirect('products:product_list')



def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    total = sum(item.product.price * item.quantity for item in items)

    return render(request, "cart/cart.html", {
        "items": items,
        "total": total
    })

