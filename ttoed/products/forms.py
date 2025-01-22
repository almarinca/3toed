from django import forms

from .models import Product


class productForm(forms.Form):
    name = forms.CharField(max_length=200, label="Name")
    description = forms.CharField(max_length=300, label="Description")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Price")
    available = forms.BooleanField(initial=True, label="Available", required=False)
    image = forms.ImageField(label="Product Image", required=False)

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            image=self.cleaned_data["image"],
        )
