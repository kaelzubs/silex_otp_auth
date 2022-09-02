"""
WSGI config for silex_otp_auth project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'silex_otp_auth.settings')

# application = get_wsgi_application()


import os
import sys
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application


path = '/home/kaelzubs/OTP_DJANGO/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'silex_otp_auth.settings'


application = get_wsgi_application()

application = WhiteNoise(application, root='/home/kaelzubs/OTP_DJANGO/silex_otp_auth/static')
application.add_files('/home/kaelzubs/OTP_DJANGO/silex_otp_auth/static/img/', prefix='static_img')
