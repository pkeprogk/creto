from django.shortcuts import render
from .models import ProductBicycle


def index(request):
    bicycles = ProductBicycle.objects.all()
    context = {'bicycles': bicycles}
    return render(request, 'store/index.html', context)


def contacts(request):

    return render(request, 'store/contacts.html')
