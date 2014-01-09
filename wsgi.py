import os
import sys

normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))

PROJECT_ROOT = normpath(__file__, "..")

# BEGIN activacte virtualenv
activate_path = normpath(PROJECT_ROOT, 'env/bin/activate_this.py')
if os.path.exists(activate_path):
    execfile(activate_path, dict(__file__=activate_path))
# END activacte virtualenv

if os.path.exists(normpath(PROJECT_ROOT, "rosetta_translator", "settings.py")):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rosetta_translator.settings")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rosetta_translator.root_settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()