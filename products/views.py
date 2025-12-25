from django.shortcuts import render
from django.db.models import Q
from .models import Product, Category
from orders.models import OrderItem


def product_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category')

    products = Product.objects.all()

    # 🔎 Search
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    # 🧭 Category filter
    if category_id:
        products = products.filter(category_id=category_id)

    # 🤖 Recommendations
    if request.user.is_authenticated:
        recommended = Product.objects.filter(
            orderitem__order__user=request.user
        ).exclude(id__in=products).distinct()[:5]
    else:
        recommended = []

    categories = Category.objects.all()

    return render(request, "products/product_list.html", {
        "products": products,
        "categories": categories,
        "query": query,
        "recommended": recommended
    })
