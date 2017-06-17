"""module4inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from apps.order.views import order_list
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^customer/', include ('apps.customer.urls', namespace="customer")),
    url(r'^order/', include ('apps.order.urls', namespace="order")),
    url(r'^member/', include ('apps.member.urls', namespace="member")),
    url(r'^accounts/login/', login, {'template_name':'index.html'}, name="login"),
 #   url(r'^$', login, {'template_name':'index.html'}, name="login"),
    url(r'^$', login_required(order_list), name='order_list'),
    url(r'^logout/', logout_then_login, name="logout"),


]
