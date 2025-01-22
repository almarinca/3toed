from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import productForm

class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = productForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
