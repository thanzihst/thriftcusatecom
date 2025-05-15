from ecommerce.wsgi import app

# Handler for Vercel serverless function
def handler(request, **kwargs):
    return app(request, **kwargs) 