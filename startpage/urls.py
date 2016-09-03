from django.conf.urls import url
from startpage.views import IndexView

app_name = 'startpage'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name="home_page"),
]