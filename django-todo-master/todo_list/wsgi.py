"""
WSGI config for todo_list project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from app import app
from django.core.wsgi import get_wsgi_application

if __name__=="__main__":
    port=int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_list.settings')

application = get_wsgi_application()
