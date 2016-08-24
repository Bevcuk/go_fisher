from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Customer


class UserInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'Додаткова інформація'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)
# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)