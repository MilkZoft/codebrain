import os
import sys
sys.path.append('/home/czantany/public_html/codebrain.org')
os.environ['DJANGO_SETTINGS_MODULE'] = 'codesbrain.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
