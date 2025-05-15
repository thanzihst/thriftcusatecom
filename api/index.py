import json

def handler(request, response):
    """Simple handler that returns a basic HTML page"""
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ThriftCUSAT - Coming Soon</title>
        <style>
            body {
                font-family: 'Helvetica Neue', Arial, sans-serif;
                background-color: #f8f9fa;
                color: #212529;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                text-align: center;
            }
            .container {
                max-width: 800px;
                padding: 40px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #007bff;
                font-size: 3rem;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.2rem;
                line-height: 1.5;
                margin-bottom: 20px;
            }
            .logo {
                max-width: 150px;
                margin-bottom: 30px;
            }
            .features {
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
                margin-top: 40px;
            }
            .feature {
                width: 200px;
                margin: 10px;
            }
            .feature h3 {
                color: #343a40;
            }
            .cta {
                display: inline-block;
                background-color: #007bff;
                color: white;
                padding: 12px 30px;
                border-radius: 30px;
                text-decoration: none;
                font-weight: bold;
                margin-top: 20px;
                transition: background-color 0.3s;
            }
            .cta:hover {
                background-color: #0056b3;
            }
            .social {
                margin-top: 30px;
            }
            .social a {
                margin: 0 10px;
                color: #6c757d;
                text-decoration: none;
                font-size: 1.5rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>ThriftCUSAT</h1>
            <p>Our e-commerce platform is currently under maintenance. We're working hard to bring you an amazing shopping experience!</p>
            
            <div class="features">
                <div class="feature">
                    <h3>Sustainable Shopping</h3>
                    <p>Pre-loved items that save the planet.</p>
                </div>
                <div class="feature">
                    <h3>Campus Community</h3>
                    <p>By students, for students.</p>
                </div>
                <div class="feature">
                    <h3>Great Deals</h3>
                    <p>Quality items at affordable prices.</p>
                </div>
            </div>
            
            <p>We'll be back online shortly with our full site. Thank you for your patience!</p>
            
            <div class="social">
                <p>Contact: info@thriftcusat.com</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": html
    } 