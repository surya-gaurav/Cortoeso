# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .generators import *


class ShortURL(models.Model):
	url = models.TextField()
	short_url = models.CharField(max_length = 10)

	def save(self, *args, **kwargs):
		if self.short_url is None or self.short_url == "":
			self.short_url = create_short_code(self)
		super(ShortURL, self).save(*args, **kwargs)

	def __str__(self):
		return self.url
