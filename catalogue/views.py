from django.views.generic import TemplateView
from catalogue.models import Category
from catalogue.models import Subcategory
from product.models import ProductFrom
from product.models import Product

class Catalogue(TemplateView):
    template_name = "catalogue.html"

    def get_context_data(self, **kwargs):
        context = super(Catalogue, self).get_context_data()
        context['category_list'] = Category.objects.all()
        context['subcategory_list'] = Subcategory.objects.all()
        context['comb_list'] = ProductFrom.objects.all()
        return context

class ProductsPage(TemplateView):
    template_name = "products_page.html"

    def get_context_data(self, **kwargs):
        context = super(ProductsPage, self).get_context_data()
        context['products'] = Product.objects.filter(from_id__subcategory_id__slug=self.kwargs['subcategory_slug'])
        context['products_brands'] = Product.objects.filter(from_id__subcategory_id__slug=self.kwargs['subcategory_slug']).\
            order_by('brand__name').values_list('brand__name', flat=True).distinct()
        context['category'] = ProductFrom.objects.get(subcategory_id__slug=self.kwargs['subcategory_slug'])
        context['subcategories'] = ProductFrom.objects.all()
        return context