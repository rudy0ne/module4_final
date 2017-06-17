from django.conf.urls import url


from apps.member.views import RegisterMember

urlpatterns = [
	url(r'^registration', RegisterMember.as_view(), name="registration")

]