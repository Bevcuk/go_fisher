from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from catalogue.views import Catalogue
from catalogue.views import ProductsPage

app_name = 'catalogue'
urlpatterns = [
    url(r'^$', Catalogue.as_view(), name='catalog_main'),
    url(r'^(?P<category_slug>\w+)-(?P<subcategory_slug>\w+)$', ProductsPage.as_view(), name='products_page'),
]
