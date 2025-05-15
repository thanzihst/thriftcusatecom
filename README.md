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