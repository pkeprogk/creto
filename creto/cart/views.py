from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import ProductBicycle
from .cart import Cart, Wishlist
from .forms import CartAddProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@require_POST
def cart_add(request, product_id):
    if 'cart' in request.POST:
        cart = Cart(request)
        product = get_object_or_404(ProductBicycle, id=product_id)
        form = CartAddProductForm(request.POST, product_id=product_id)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd['quantity'],
                     frame_size=cd['frame_size'],
                     wheel_size=cd['wheel_size'],
                     update_quantity=cd['update'])
        return redirect('cart-detail')
    elif 'wishlist' in request.POST:
        wishlist = Wishlist(request)
        product = get_object_or_404(ProductBicycle, id=product_id)
        form = CartAddProductForm(request.POST, product_id=product_id)
        if form.is_valid():
            cd = form.cleaned_data
            wishlist.add(product=product,
                         quantity=cd['quantity'],
                         frame_size=cd['frame_size'],
                         wheel_size=cd['wheel_size'],
                         update_quantity=cd['update'])
        return redirect('wishlist-detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductBicycle, id=product_id)
    cart.remove(product)
    return redirect('cart-detail')


def cart_detail(request):
    cart = Cart(request)
    page = request.GET.get('page')
    results = 8
    products = cart.get_products()
    paginator = Paginator(products, results)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        products = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        products = paginator.page(page)

    page = int(page)
    left_index = page - 3 if page > 3 else 1

    right_index = page + 4 if page < paginator.num_pages - 3 else paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    context = {
        'cart': cart,
        'products': products,
        'paginator': paginator,
        'custom_range': custom_range
    }
    return render(request, 'cart/cart-detail.html', context)


def wishlist_remove(request, product_id):
    wishlist = Wishlist(request)
    product = get_object_or_404(ProductBicycle, id=product_id)
    wishlist.remove(product)
    return redirect('wishlist-detail')


def wishlist_detail(request):
    wishlist = Wishlist(request)
    page = request.GET.get('page')
    results = 8
    products = wishlist.get_products()
    paginator = Paginator(products, results)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        products = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        products = paginator.page(page)

    page = int(page)
    left_index = page - 3 if page > 3 else 1

    right_index = page + 4 if page < paginator.num_pages - 3 else paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    context = {
        'wishlist': wishlist,
        'products': products,
        'paginator': paginator,
        'custom_range': custom_range
    }
    return render(request, 'cart/wishlist-detail.html', context)
