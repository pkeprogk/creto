from django.shortcuts import render
from .models import ProductBicycle


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
