from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from cart.forms import CartAddProductForm
from store.forms import *


def index(request):
    bicycles = ProductBicycle.objects.all()
    bicycle_types = ProductBicycle.objects.values_list('bicycle_type', flat=True).distinct()
    bicycle_classes = ProductBicycle.objects.values_list('bicycle_class', flat=True).distinct()
    bicycle_brands = ProductBicycle.objects.values_list('bicycle_brand', flat=True).distinct()
    context = {'bicycles': bicycles,
               'bicycle_types': bicycle_types,
               'bicycle_classes': bicycle_classes,
               'bicycle_brands': bicycle_brands,
               }
    return render(request, 'store/index.html', context)


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            phone = form.cleaned_data['your_phone']
            email = form.cleaned_data['your_email']
            comments = form.cleaned_data['your_text']

            Message.objects.create(
                name=name,
                phone=phone,
                email=email,
                comments=comments
            )
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'store/contacts.html', {'form': form})


def news(request):
    return render(request, 'store/news.html')


def shop(request):
    bicycles = ProductBicycle.objects.all()
    accessories = ProductAccessory.objects.all()
    clothes = ProductClothes.objects.all()
    spare_parts = ProductSparePart.objects.all()
    context = {
        'bicycles': bicycles,
        'accessories': accessories,
        'clothes': clothes,
        'spare_parts': spare_parts
    }

    return render(request, 'store/shop.html', context)


def shop_bicycles(request):
    page = request.GET.get('page')
    results = 6
    sort_param = request.GET.get('sort', '')

    filter_form = BicycleFilterForm(request.GET)

    if sort_param == 'price':
        bicycles = ProductBicycle.objects.all().order_by('bicycle_price_new')
    elif sort_param == 'price_desc':
        bicycles = ProductBicycle.objects.all().order_by('-bicycle_price_new')
    else:
        bicycles = ProductBicycle.objects.all()

    if filter_form.is_valid():
        brand = filter_form.cleaned_data.get('brand')
        bicycle_type = filter_form.cleaned_data.get('bicycle_type')
        min_price = filter_form.cleaned_data.get('min_price')
        max_price = filter_form.cleaned_data.get('max_price')

        if brand:
            bicycles = bicycles.filter(bicycle_brand=brand)

        if bicycle_type:
            bicycles = bicycles.filter(bicycle_type=bicycle_type)

        if min_price is not None:
            bicycles = bicycles.filter(bicycle_price_new__gte=min_price)

        if max_price is not None:
            bicycles = bicycles.filter(bicycle_price_new__lte=max_price)

    bicycle_types = ProductBicycle.objects.values_list('bicycle_type', flat=True).distinct()
    bicycle_brands = ProductBicycle.objects.values_list('bicycle_brand', flat=True).distinct()

    paginator = Paginator(bicycles, results)
    try:
        bicycles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        bicycles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        bicycles = paginator.page(page)

    page = int(page)
    left_index = page - 3 if page > 3 else 1

    right_index = page + 4 if page < paginator.num_pages - 3 else paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    context = {
        'bicycles': bicycles,
        'bicycle_types': bicycle_types,
        'bicycle_brands': bicycle_brands,
        'paginator': paginator,
        'custom_range': custom_range,
        'filter_form': filter_form,
    }

    return render(request, 'store/shop-bicycles.html', context)


def shop_accessories(request):
    accessories = ProductAccessory.objects.all()
    accessories_types = ProductAccessory.objects.values_list('accessory_type', flat=True).distinct()
    accessories_prices = ProductAccessory.objects.values_list('accessory_price', flat=True).distinct()
    accessories_brands = ProductAccessory.objects.values_list('accessory_brand', flat=True).distinct()
    context = {
        'accessories': accessories,
        'accessories_types': accessories_types,
        'accessories_prices': accessories_prices,
        'accessories_brands': accessories_brands
    }

    return render(request, 'store/shop-accessories.html', context)


def shop_spare_parts(request):
    spare_parts = ProductSparePart.objects.all()
    spare_parts_types = ProductSparePart.objects.values_list('spare_part_type', flat=True).distinct()
    spare_parts_prices = ProductSparePart.objects.values_list('spare_part_price', flat=True).distinct()
    spare_parts_brands = ProductSparePart.objects.values_list('spare_part_brand', flat=True).distinct()
    context = {
        'spare_parts': spare_parts,
        'spare_parts_types': spare_parts_types,
        'spare_parts_prices': spare_parts_prices,
        'spare_parts_brands': spare_parts_brands
    }

    return render(request, 'store/shop-spare-parts.html', context)


def shop_clothes(request):
    clothes = ProductClothes.objects.all()
    clothes_types = ProductClothes.objects.values_list('clothes_type', flat=True).distinct()
    clothes_prices = ProductClothes.objects.values_list('clothes_price', flat=True).distinct()
    clothes_brands = ProductClothes.objects.values_list('clothes_brand', flat=True).distinct()
    clothes_sexes = ProductClothes.objects.values_list('clothes_sex', flat=True).distinct()
    context = {
        'clothes': clothes,
        'accessories_types': clothes_types,
        'accessories_prices': clothes_prices,
        'accessories_brands': clothes_brands,
        'accessories_sexes': clothes_sexes
    }

    return render(request, 'store/shop-clothes.html', context)


def single_bicycle(request, pk):
    bicycle = ProductBicycle.objects.get(pk=pk)
    cart_product_form = CartAddProductForm(product_id=pk)

    context = {
        'bicycle': bicycle,
        'cart_product_form': cart_product_form
    }

    return render(request, 'store/single-bicycle.html', context)
