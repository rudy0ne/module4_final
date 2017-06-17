from django import forms

from apps.order.models import Order



class OrderForm(forms.ModelForm):

	class Meta:
		model = Order

		fields = [
#			'created_at',
			'customer',
			'product',
		]
		labels = {
#			'created_at': 'placed on',
			'customer': 'choose customer name',
			'product': 'items',
		}
		widgets = {
#			'created_at': forms.TextInput(attrs={'class':'form-control'}),
			'customer': forms.Select(attrs={'class':'form-control'}),
			'product': forms.CheckboxSelectMultiple(),

		}