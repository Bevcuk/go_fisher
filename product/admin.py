from django.contrib import admin

from .models import Product
from .models import ProductFrom
from .models import Brand
from .models import Special
from .models import Image
from .models import Kind


class ProductAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'js/jquery-latest.min.js',
            'js/adminscripts.js',
        )

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductFrom)
admin.site.register(Brand)
admin.site.register(Special)
admin.site.register(Image)
admin.site.register(Kind)
