from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required


from apps.order.views import index, order_view, order_list, order_edit, order_delete

app_name = 'order'
urlpatterns = [
	url(r'^$', login_required(order_list), name='order_list'),
	url(r'^new$', login_required(order_view), name='order_create'),
	url(r'^list$', login_required(order_list), name='order_list'),



	url(r'^edit/(?P<id_order>\d+)/$', login_required(order_edit), name='order_edit'),
	url(r'^delete/(?P<id_order>\d+)/$', login_required(order_delete), name='order_delete'),

]
