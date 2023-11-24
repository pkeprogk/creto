from django import forms
from store.models import ProductBicycle

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]


class CartAddProductForm(forms.Form):
    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id')
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        product = ProductBicycle.objects.get(pk=product_id)
        self.FRAME_SIZE_CHOICES = [(size, size) for size in product.bicycle_frame_sizes.all()]
        self.WHEEL_SIZE_CHOICES = [(size, size) for size in product.bicycle_wheel_sizes.all()]

        self.fields['quantity'] = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int,
                                                         widget=forms.Select(attrs={'class': 'nice-select'}))
        self.fields['frame_size'] = forms.TypedChoiceField(choices=self.FRAME_SIZE_CHOICES,
                                                           widget=forms.Select(attrs={'class': 'nice-select'}))
        self.fields['wheel_size'] = forms.TypedChoiceField(choices=self.WHEEL_SIZE_CHOICES,
                                                           widget=forms.Select(attrs={'class': 'nice-select'}))
        self.fields['update'] = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
