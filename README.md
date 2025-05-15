# THRIFTCUSAT E-commerce

A premium e-commerce platform for CUSAT, built with Django and featuring a sophisticated black and white aesthetic.

## Features

- Modern, responsive design with black and white aesthetic
- Product catalog with categories
- Detailed product pages with image galleries
- WhatsApp integration for direct purchases
- Mobile-responsive navigation
- Announcement bar for important updates
- SEO-friendly URLs
- Admin interface for content management

## Tech Stack

- Django 5.0.1
- Python 3.13
- PostgreSQL (Production)
- WhiteNoise for static files
- Tailwind CSS
- Responsive Images
- Modern JavaScript

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/thriftcusat.git
cd thriftcusat
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the root directory and add your environment variables:
```
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the application.

## Deployment

The project is configured for deployment on any Python-compatible hosting platform. See `production.py` for production settings.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - [@thrift.cusat](https://instagram.com/thrift.cusat)

Project Link: [https://github.com/yourusername/thriftcusat](https://github.com/yourusername/thriftcusat)

## Deploying to Heroku

### Automatic Deployment

We've created a simple script to help deploy this application to Heroku:

1. Make sure you have committed all your changes to git
2. Run the deployment script:
   ```
   ./deploy_to_heroku.sh
   ```
3. Follow the prompts to log in to Heroku and enter your custom domain

### Manual Deployment Steps

If you prefer to deploy manually, follow these steps:

1. Install the Heroku CLI:
   ```
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. Log in to Heroku:
   ```
   heroku login
   ```

3. Create a new Heroku app:
   ```
   heroku create thriftcusat
   ```

4. Add PostgreSQL:
   ```
   heroku addons:create heroku-postgresql:mini
   ```

5. Configure environment variables:
   ```
   heroku config:set DJANGO_SETTINGS_MODULE=ecommerce.heroku_settings
   heroku config:set PYTHONUNBUFFERED=1
   ```

6. Add your custom domain:
   ```
   heroku domains:add yourdomain.com
   ```

7. Push to Heroku:
   ```
   git push heroku main
   ```

8. Run migrations:
   ```
   heroku run python manage.py migrate
   ```

9. Create a superuser:
   ```
   heroku run python manage.py createsuperuser
   ```

## Setting Up Custom Domain

After adding your domain to Heroku with `heroku domains:add yourdomain.com`, you'll need to configure your DNS:

1. Get your DNS target from Heroku:
   ```
   heroku domains:info
   ```

2. Add a CNAME record with your DNS provider:
   - Name: @ or subdomain (e.g., www)
   - Value: The DNS target from Heroku (ending in herokudns.com)

3. Wait for DNS propagation (may take up to 24 hours)

## Local Development

1. Clone the repository:
   ```
   git clone https://github.com/thanzihst/thriftcusatecom.git
   cd thriftcusatecom
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ``` 