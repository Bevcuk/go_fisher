from django.conf.urls import url
from startpage.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="home_list"),
]