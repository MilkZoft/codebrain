from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from apps.blog.models import Blog
from apps.blog import *
from apps.blog.forms import *

def index(request):
	if request.method == 'POST':
		postsForm = PostsForm(request.POST);

		if postsForm.is_valid():
			postsForm.save();

			return HttpResponseRedirect('/')
	
	else:
		postsForm = PostsForm()

def getAllPosts(request):
	return render_to_response('posts.html', RequestContext(request, locals()))