from ecommerce.wsgi import application

async def handler(request):
    """
    Serverless handler for Vercel
    """
    if hasattr(request, 'body'):
        body = await request.body() if request.body else b''
    else:
        body = b''

    environ = {
        'REQUEST_METHOD': request.method,
        'SCRIPT_NAME': '',
        'PATH_INFO': request.url.path,
        'QUERY_STRING': str(request.url.query),
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': body,
        'wsgi.errors': None,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
        'HTTP_HOST': request.headers.get('host', ''),
        'HTTP_USER_AGENT': request.headers.get('user-agent', ''),
        'HTTP_ACCEPT': request.headers.get('accept', ''),
        'HTTP_ACCEPT_LANGUAGE': request.headers.get('accept-language', ''),
        'HTTP_ACCEPT_ENCODING': request.headers.get('accept-encoding', ''),
        'HTTP_COOKIE': request.headers.get('cookie', ''),
        'HTTP_CONNECTION': request.headers.get('connection', ''),
        'REMOTE_ADDR': request.headers.get('x-real-ip', request.headers.get('x-forwarded-for', '')),
        'CONTENT_TYPE': request.headers.get('content-type', ''),
        'CONTENT_LENGTH': request.headers.get('content-length', ''),
    }

    response = []

    def start_response(status, headers):
        response.append({
            'status': status,
            'headers': headers,
        })

    result = application(environ, start_response)
    
    if not response:
        return {'statusCode': 500, 'body': 'Internal Server Error'}

    body = b''.join(result) if isinstance(result, (list, tuple)) else result
    
    return {
        'statusCode': int(response[0]['status'].split()[0]),
        'headers': dict(response[0]['headers']),
        'body': body.decode('utf-8') if isinstance(body, bytes) else str(body)
    } 