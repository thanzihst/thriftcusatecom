from ecommerce.wsgi import app

def handler(request):
    """Handle incoming HTTP requests in Vercel's serverless environment"""
    if not hasattr(request, 'environ'):
        # Create a minimal WSGI environment if not present
        request.environ = {
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'https',
            'wsgi.input': None,
            'wsgi.errors': None,
            'wsgi.multithread': False,
            'wsgi.multiprocess': False,
            'wsgi.run_once': False,
            'SERVER_SOFTWARE': 'Vercel',
            'REQUEST_METHOD': request.method,
            'PATH_INFO': request.path,
            'QUERY_STRING': request.query_string.decode() if hasattr(request, 'query_string') else '',
        }
    return app(request.environ, lambda x, y: None) 