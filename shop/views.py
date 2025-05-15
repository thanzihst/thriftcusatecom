from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Product, Category

# Create your views here.

def home(request):
    # Get featured products (latest 8 products)
    featured_products = Product.objects.filter(available=True).order_by('-created')[:8]
    categories = Category.objects.all()

    context = {
        'featured_products': featured_products,
        'categories': categories,
    }
    
    return render(request, 'shop/home.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    
    context = {
        'product': product,
        'whatsapp_number': getattr(settings, 'WHATSAPP_NUMBER', '+919747570987'),
    }
    
    return render(request, 'shop/product_detail.html', context)

def product_list(request):
    category_slug = request.GET.get('category')
    sort = request.GET.get('sort', '')
    
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Apply sorting
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': category_slug,
        'sort': sort,
    }
    
    return render(request, 'shop/products.html', context)
