from decimal import Decimal
from django.conf import settings
from store.models import ProductBicycle


class Cart(object):

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, product, quantity=1, frame_size=0, wheel_size=0, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'frame_size': frame_size,
                                     'wheel_size': wheel_size,
                                     'price': str(product.bicycle_price_new)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = ProductBicycle.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_products(self):
        product_ids = self.cart.keys()
        products = ProductBicycle.objects.filter(id__in=product_ids)
        return products


class Wishlist(object):

    def __init__(self, request):

        self.session = request.session
        wishlist = self.session.get(settings.WISHLIST_SESSION_ID)

        if not wishlist:
            wishlist = self.session[settings.WISHLIST_SESSION_ID] = {}

        self.wishlist = wishlist

    def add(self, product, quantity=1, frame_size=0, wheel_size=0, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.wishlist:
            self.wishlist[product_id] = {'quantity': 0,
                                         'frame_size': frame_size,
                                         'wheel_size': wheel_size,
                                         'price': str(product.bicycle_price_new)}
        if update_quantity:
            self.wishlist[product_id]['quantity'] = quantity
        else:
            self.wishlist[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.WISHLIST_SESSION_ID] = self.wishlist
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.wishlist:
            del self.wishlist[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.wishlist.keys()
        products = ProductBicycle.objects.filter(id__in=product_ids)
        for product in products:
            self.wishlist[str(product.id)]['product'] = product

        for item in self.wishlist.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.wishlist.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.wishlist.values())

    def clear(self):
        del self.session[settings.WISHLIST_SESSION_ID]
        self.session.modified = True

    def get_products(self):
        product_ids = self.wishlist.keys()
        products = ProductBicycle.objects.filter(id__in=product_ids)
        return products
