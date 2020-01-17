"""
WSGI config for django_practice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
import logging



from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_practice.settings")

#sys.path.append('/home/ubuntu/projects/django_practice')
#sys.path.append('/home/ubuntu/projects/django_practice/django_practice')
import pymysql
pymysql.install_as_MySQLdb()

application = get_wsgi_application()


def applicationxx(environ, start_response):
    status = '200 OK'
    output = u'mod_wsgi.application_group = %s' % sys.path
    #output = u'mod_wsgi.application_group = %s' % repr(environ['mod_wsgi.application_group'])

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output.encode('UTF-8')]
