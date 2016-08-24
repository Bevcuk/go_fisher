from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from product.views import Product_details

app_name = 'product'
urlpatterns = [
    url(r'^details/(?P<pk>\d+)/$', Product_details.as_view(), name='product_details'),
]