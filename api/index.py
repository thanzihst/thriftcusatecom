from http.server import BaseHTTPRequestHandler
import os

# Set environment variables
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings_prod")

# Import Django application
from ecommerce.wsgi import application

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Hello, World!'.encode())
        return

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Received POST request'.encode())
        return 