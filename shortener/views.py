# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, Http404
from .forms import SubmitForm
from django.views import View
from .models import ShortURL
from .generators import *


class Home(View):
	form_class = SubmitForm
	home_template = 'home.html'
	shorten_template = 'shorturl.html'
	already_exists = 'exist.html'
	error = 'error.html'
	initial = {'key' : 'value'}

	def get(self, request, *args, **kwargs):
		form = self.form_class(initial = self.initial)
		return render(request, self.home_template, {'form' : form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)

		if form.is_valid():
			new_url = form.cleaned_data.get('url')
			valid_domains = ['.com', '.in', '.co', '.org']
			count = 0
			for i in range(len(valid_domains)):
				if valid_domains[i] not in new_url:
					count = count+1

			if count==4:
				return render(request, self.error, None)
			if not 'http' in new_url:
				new_url = 'http://' + new_url
			obj, created = ShortURL.objects.get_or_create(url = new_url)
			
			if created == True:
				return render(request, self.shorten_template, {'data' : obj})
			else:
				return render(request, self.already_exists, {'data' : obj})
		else:
			return render(request, self.home_template, {})

class URLRedirectView(View):
	def get(self, request, short_url=None, *args, **kwargs):
		qs = ShortURL.objects.filter(short_url__iexact=short_url)
		if qs.count() != 1 and not qs.exists():
			raise Http404
		qs = qs.first()
		return HttpResponseRedirect(qs)

