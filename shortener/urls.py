from django.conf.urls import url
from shortener.views import Home, URLRedirectView
urlpatterns = [
	url(r'^$', Home.as_view()),
	url(r'^(?P<short_url>[\w-]+)/$', URLRedirectView.as_view(), name='scode')
]