from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from apps.blog.models import Blog
from apps.blog import *

def getAllPosts(request):
	return render_to_response('posts.html', RequestContext(request, locals()))