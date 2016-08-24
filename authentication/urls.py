from django.conf.urls import include, url

from . import views

app_name = 'authentication'
urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^register/', views.register_user, name='register'),
    url(r'^register_success/', views.register_success),
    url(r'^confirm/(?P<activation_key>.+)$', views.register_confirm),
]