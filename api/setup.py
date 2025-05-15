import os
import sys
import django
from django.core.management import call_command

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings_prod")
django.setup()

# Collect static files
call_command("collectstatic", verbosity=1, interactive=False)

print("Environment setup complete") 