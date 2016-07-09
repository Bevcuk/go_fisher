from django.contrib import admin

from .models import BigCategory
from .models import Category
from .models import Subcategory

admin.site.register(BigCategory)
admin.site.register(Category)
admin.site.register(Subcategory)
