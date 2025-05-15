#!/bin/bash

# Exit on error
set -e

echo "==== ThriftCUSAT Heroku Deployment Script ===="
echo

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "Heroku CLI not found. Installing..."
    # Install Heroku CLI
    curl https://cli-assets.heroku.com/install.sh | sh
else
    echo "Heroku CLI already installed."
fi

# Check if logged in to Heroku
if ! heroku auth:whoami &> /dev/null; then
    echo "Please log in to Heroku:"
    heroku login
else
    echo "Already logged in to Heroku."
fi

# Check if app exists
APP_NAME="thriftcusat"
if ! heroku apps:info --app $APP_NAME &> /dev/null; then
    echo "Creating Heroku app '$APP_NAME'..."
    heroku create $APP_NAME
else
    echo "Heroku app '$APP_NAME' already exists."
fi

# Add PostgreSQL
echo "Ensuring PostgreSQL addon is available..."
if ! heroku addons:info --app $APP_NAME postgresql &> /dev/null; then
    heroku addons:create --app $APP_NAME heroku-postgresql:mini
fi

# Set environment variables
echo "Setting environment variables..."
heroku config:set --app $APP_NAME DJANGO_SETTINGS_MODULE=ecommerce.settings_prod
heroku config:set --app $APP_NAME PYTHONUNBUFFERED=1
heroku config:set --app $APP_NAME DISABLE_COLLECTSTATIC=0

# Ask for domain name
read -p "Enter your custom domain name (e.g., thriftcusat.com): " DOMAIN_NAME
if [ ! -z "$DOMAIN_NAME" ]; then
    heroku config:set --app $APP_NAME DOMAIN_NAME=$DOMAIN_NAME
    echo "Adding domain to Heroku..."
    heroku domains:add --app $APP_NAME $DOMAIN_NAME
    echo
    echo "IMPORTANT: Set up the following DNS records with your domain provider:"
    heroku domains:info --app $APP_NAME
fi

# Push to Heroku
echo
echo "Deploying to Heroku..."
git push heroku main

echo
echo "==== Deployment Complete ===="
echo "Your app should be available at: https://$APP_NAME.herokuapp.com"
if [ ! -z "$DOMAIN_NAME" ]; then
    echo "Once DNS is set up, it will also be available at: https://$DOMAIN_NAME"
fi 