from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic import TemplateView
from product.models import Product

# Create your views here.

class Product_details(TemplateView):
    context_object_name = 'products'
    template_name = 'product.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Product_details, self).get_context_data()
        context['product'] = Product.objects.get(pk=1)
        context['kinds'] = Product.objects.get(pk=1).kind.all()
        context['images'] = Product.objects.get(pk=1).image.all()
        context['recommendations'] = Product.objects.all()[:3]
        context['popular'] = Product.objects.all()[:4]
        return context