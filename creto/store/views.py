from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
    return render(request, 'store/contacts.html')


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
    bicycles = ProductBicycle.objects.all()
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
        'custom_range': custom_range
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

    context = {
        'bicycle': bicycle
    }

    return render(request, 'store/single-bicycle.html', context)
