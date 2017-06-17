from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.order.forms import OrderForm
from apps.order.models import Order

	# Create your views here.

def index(request):
	return render(request, 'order/order.html')


def order_view(request):
	if request.method == 'POST':
		form = OrderForm(request.POST)	
		if form.is_valid():
			form.save()
		return redirect('order:order_list')
	else:
		form = OrderForm()

	return render(request, 'order/order_form.html', {'form':form})

def order_list(request):
	order = Order.objects.all().order_by('id')
	context = {'orders':order}
	return render(request, 'order/order_list.html', context)


	 		
def order_edit(request, id_order):
	order = Order.objects.get(id=id_order)
	if request.method == 'GET':
		form = OrderForm(instance=order)
	else: 
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
		return redirect('order:order_list')
	return render(request, 'order/order_form.html', {'form':form})	


def order_delete(request, id_order):
	order = Order.objects.get(id=id_order)
	if request.method == 'POST':
		order.delete()
		return redirect('order:order_list')
	return render(request, 'order/order_delete.html', {'order':order})



