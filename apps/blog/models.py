# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.utils.translation import ugettext as _

class Blog(models.Model):
	title 			= models.CharField(_('Title'), max_length = 250)
	slug 			= models.CharField(_('Slug'), max_length = 250)
	content 		= models.TextField()
	tags 			= models.CharField(_('Tags'), max_length = 100)
	author 			= models.CharField(_('Tags'), max_length = 50)
	creation_date 	= models.DateField("Creation Date", default = datetime.today)
	year 			= models.CharField(_('Tags'), max_length = 4)
	month 			= models.CharField(_('Month'), max_length = 2)
	day 			= models.CharField(_('Day'), max_length = 2)
	image 			= models.CharField(_('Image'), max_length = 250)
	image_thumbnail = models.CharField(_('Image Thumbnail'), max_length = 250)
	image_preview 	= models.CharField(_('Image Preview'), max_length = 250)
	views 			= models.IntegerField(_('Views'))
	comments 		= models.IntegerField(_('Comments'))
	enable_comments = models.BooleanField(default = True)
	language 		= models.CharField(_('Language'), max_length = 20)
	display_bio 	= models.BooleanField(default = True)
	bufferapp 		= models.BooleanField(default = True)
	situation 		= models.CharField(_('Situation'), max_length = 15)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = _('Post')
		verbose_name_plural = _('Posts')