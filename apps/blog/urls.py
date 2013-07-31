from django.conf.urls.defaults import *

urlpatterns = patterns(
	'apps.blog.views',
	url(r'^blog/', 'getAllPosts'),
)