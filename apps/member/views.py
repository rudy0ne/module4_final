from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.member.forms import RegistrationForm


class RegisterMember(CreateView):
	model = User
	template_name = "member/registration.html"
	form_class = RegistrationForm
	success_url = reverse_lazy('order:order_create')
