from django.conf.urls import url

from apps.customer.views import index

app_name = 'customer'
urlpatterns = [
    url(r'^$', index),

]
