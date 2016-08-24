from django.contrib import admin

from .models import BigCategory
from .models import Category
from .models import Subcategory


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(BigCategory)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubCategoryAdmin)

