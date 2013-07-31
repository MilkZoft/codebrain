from django.forms import ModelForm
from apps.blog.models import *

class PostsForm(ModelForm):
	class Meta:
		model = Posts