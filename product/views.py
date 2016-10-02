from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from product.models import Product

# Create your views here.

class Product_details(DetailView):
    context_object_name = 'product'
    template_name = 'product.html'
    # ??? do you really need it
    # queryset = Product.objects.all()

    def get_queryset(self):
        self.product = get_object_or_404(Product, pk=self.kwargs['pk'])
        return Product.objects.filter(pk=self.product.id)

    def get_context_data(self, **kwargs):
        context = super(Product_details, self).get_context_data()
        context['product'] = self.product
        context['kinds'] = Product.objects.get(pk=self.product.id).kind.all()
        context['images'] = Product.objects.get(pk=self.product.id).image.all()
        context['recommendations'] = Product.objects.all()[:3]
        context['popular'] = Product.objects.all()[:4]
        return context