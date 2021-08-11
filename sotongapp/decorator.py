from pathlib import Path
import os, environ

from django.http import HttpResponseForbidden

from sotongapp.encrypt import RSA_dec


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))


# def organ_permission_check(func):
#     def decorated(request, *args, **kwargs):
#         if RSA_dec(request.headers.get('Cookie', '')) != env('PEM_SECRET'):
#             return HttpResponseForbidden
#         return func(request, *args, **kwargs)

#     return decorated
