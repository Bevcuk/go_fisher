from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from catalogue.views import Catalogue
from catalogue.views import ProductsPage
from catalogue.views import FilteredProductsPage

app_name = 'catalogue'
urlpatterns = [
    url(r'^$', Catalogue.as_view(), name='catalog_main'),
    url(r'^(?P<category_slug>[\w-]+)_(?P<subcategory_slug>[\w-]+)$', ProductsPage.as_view(), name='products_page'),
    url(r'^(?P<category_slug>[\w-]+)_(?P<subcategory_slug>[\w-]+)/filter/(?P<extra_params>[\w\D]+)$', FilteredProductsPage.as_view(), name='filtered_products'),
]
