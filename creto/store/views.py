from django.shortcuts import render
from .models import *


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
    bicycles = ProductBicycle.object.all()
    accessories = ProductAccessory.object.all()
    clothes = ProductClothes.object.all()
    spare_parts = ProductSparePart.object.all()
    context = {
        'bicycles': bicycles,
        'accessories': accessories,
        'clothes': clothes,
        'spare_parts': spare_parts
    }

    return render(request, 'store/shop.html', context)
