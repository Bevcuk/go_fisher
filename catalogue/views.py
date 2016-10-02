import operator
from functools import reduce
from django.db.models import Q

from django.views.generic import TemplateView
from django.views.generic import ListView
from catalogue.models import Category
from catalogue.models import Subcategory
from product.models import ProductFrom
from product.models import Product
from django.db.models import Max

class Catalogue(TemplateView):
    template_name = "catalogue.html"

    def get_context_data(self, **kwargs):
        context = super(Catalogue, self).get_context_data()
        context['category_list'] = Category.objects.all()
        context['subcategory_list'] = Subcategory.objects.all()
        context['comb_list'] = ProductFrom.objects.all()
        return context


class ProductsPage(ListView):
    model = Product
    template_name = "products_page.html"

    def get_context_data(self, **kwargs):
        context = super(ProductsPage, self).get_context_data()
        context['products'] = Product.objects.filter(from_id__subcategory_id__slug=self.kwargs['subcategory_slug'])
        context['max_price'] = str(Product.objects.filter(
            from_id__subcategory_id__slug=self.kwargs['subcategory_slug']).aggregate(Max('price'))['price__max']).split('.')[0]
        context['products_brands'] = Product.objects.filter(
            from_id__subcategory_id__slug=self.kwargs['subcategory_slug']). \
            order_by('brand__name').values_list('brand__name', flat=True).distinct()
        context['category'] = ProductFrom.objects.get(subcategory_id__slug=self.kwargs['subcategory_slug'])
        context['subcategories'] = ProductFrom.objects.all()
        context['extra_params'] = Subcategory.objects.get(slug=self.kwargs['subcategory_slug'])
        return context

class FilteredProductsPage(ListView):
    template_name = "products_page.html"

    def get_queryset(self, *args, **kwargs):
        extra = self.kwargs['extra_params']
        search_list = extra.split(';')
        brands = []

        if 'brand' in extra:
            # need re
            brand_partition = extra.partition('brand=')
            full_brand = brand_partition[1] + brand_partition[2].split(';')[0]
            brands = brand_partition[2].split(';')[0].split('_')
            # search params without brand
            search_list = [value for value in search_list if value != full_brand]

            # queryset = Product.objects.filter(brand__name=brands[0])
            queryset = Product.objects.filter(
                reduce(operator.or_, (Q(brand__name=x) for x in brands)))
            if search_list:
                queryset = queryset.filter(reduce(operator.and_, (Q(slug_params_json__contains=x) for x in search_list)))
            return queryset

        queryset = Product.objects.filter(reduce(operator.and_, (Q(slug_params_json__contains=x) for x in search_list)))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(FilteredProductsPage, self).get_context_data()
        context['products'] = self.get_queryset().filter(from_id__subcategory_id__slug=self.kwargs['subcategory_slug'])
        context['max_price'] = str(self.get_queryset().filter(
            from_id__subcategory_id__slug=self.kwargs['subcategory_slug']).aggregate(Max('price'))[
                                       'price__max']).split('.')[0]
        context['products_brands'] = self.get_queryset().filter(
            from_id__subcategory_id__slug=self.kwargs['subcategory_slug']). \
            order_by('brand__name').values_list('brand__name', flat=True).distinct()
        context['category'] = ProductFrom.objects.get(subcategory_id__slug=self.kwargs['subcategory_slug'])
        context['subcategories'] = ProductFrom.objects.all()
        context['extra_params'] = Subcategory.objects.get(slug=self.kwargs['subcategory_slug'])
        return context