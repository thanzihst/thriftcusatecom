from ecommerce.wsgi import application

def handler(request):
    """
    Simple handler for Vercel serverless
    """
    return application(request) 