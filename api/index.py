from http.server import BaseHTTPRequestHandler
import os
import io
import sys
from urllib.parse import parse_qs

# Set environment variables
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings_prod")

# Import Django application
from ecommerce.wsgi import application

class ServerlessHandler(BaseHTTPRequestHandler):
    def __init__(self, req, res, **kwargs):
        self.request = req
        self.path = req.get("path", "/")
        self.headers = req.get("headers", {})
        self.method = req.get("method", "GET")
        self.body = req.get("body", "")
        self.query = req.get("query", {})
        self.response = {}
        self.response_headers = []
        
    def get_environ(self):
        env = {}
        
        # Required WSGI variables
        env['wsgi.version'] = (1, 0)
        env['wsgi.url_scheme'] = 'https'
        env['wsgi.input'] = io.BytesIO(self.body.encode() if isinstance(self.body, str) else self.body)
        env['wsgi.errors'] = sys.stderr
        env['wsgi.multithread'] = False
        env['wsgi.multiprocess'] = False
        env['wsgi.run_once'] = False
        
        # HTTP headers
        for k, v in self.headers.items():
            env['HTTP_' + k.upper().replace('-', '_')] = v
            
        # Request data
        env['REQUEST_METHOD'] = self.method
        env['PATH_INFO'] = self.path
        env['QUERY_STRING'] = '&'.join([f"{k}={v}" for k, v in self.query.items()]) if isinstance(self.query, dict) else self.query or ""
        env['CONTENT_TYPE'] = self.headers.get('content-type', '')
        env['CONTENT_LENGTH'] = str(len(self.body) if self.body else 0)
        env['SERVER_NAME'] = 'vercel-serverless'
        env['SERVER_PORT'] = '443'
        
        return env
        
    def start_response(self, status, headers):
        self.response['statusCode'] = int(status.split(' ')[0])
        self.response_headers = headers
        
    def handle(self):
        env = self.get_environ()
        result = application(env, self.start_response)
        
        # Get response body
        body = b''
        for data in result:
            if data:
                body += data
                
        # Convert to string if possible
        if body:
            try:
                body = body.decode('utf-8')
            except UnicodeDecodeError:
                # If it can't be decoded, return as base64
                import base64
                body = base64.b64encode(body).decode('utf-8')
                self.response['isBase64Encoded'] = True
        
        # Set headers
        headers = {}
        for key, value in self.response_headers:
            headers[key] = value
            
        self.response['headers'] = headers
        self.response['body'] = body
        
        return self.response

def handler(req, res):
    """Handler function for Vercel serverless"""
    handler_instance = ServerlessHandler(req, res)
    return handler_instance.handle() 