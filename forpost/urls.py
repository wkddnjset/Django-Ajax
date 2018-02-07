from django.conf.urls import url
from .views import LoneListView, PaybackAjax

urlpatterns = [
    url(r'ajax/payback/(?P<pk>[\w-]+)/$', PaybackAjax, name='payback'),
    url(r'lone/$', LoneListView, name='lone-list'),
]