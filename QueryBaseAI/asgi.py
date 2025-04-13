"""
ASGI config for QueryBaseAI project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QueryBaseAI.settings')

application = get_asgi_application()
