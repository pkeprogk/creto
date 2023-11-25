from django import forms
from .models import Review


class BicycleFilterForm(forms.Form):
    brand = forms.CharField(required=False)
    bicycle_type = forms.CharField(required=False)
    min_price = forms.IntegerField(required=False)
    max_price = forms.IntegerField(required=False)


class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=255)
    your_phone = forms.CharField(max_length=20)
    your_email = forms.EmailField(max_length=255)
    your_text = forms.CharField(widget=forms.Textarea)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text']
