from django.shortcuts import render
from orders.models import Order, OrderItem
from products.models import Product
from django.db.models import Sum

def admin_dashboard(request):
    total_orders = Order.objects.count()

    revenue = OrderItem.objects.aggregate(
        total=Sum('product__price')
    )['total'] or 0

    top_products = (
        OrderItem.objects
        .values('product__name')
        .annotate(total=Sum('quantity'))
        .order_by('-total')[:5]
    )

    recent_orders = Order.objects.order_by('-created_at')[:5]

    return render(request, 'dashboard/dashboard.html', {
        'total_orders': total_orders,
        'revenue': revenue,
        'top_products': top_products,
        'recent_orders': recent_orders
    })
