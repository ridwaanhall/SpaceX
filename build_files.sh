#!/bin/bash

# Build script for Vercel deployment
echo "Starting build process..."

# Install dependencies (this should be handled by Vercel automatically)
echo "Installing Python dependencies..."
python3.12 -m pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python3.12 manage.py collectstatic --noinput --clear

echo "Build process completed!"

# Create a simple static directory for Vercel (even though we use WhiteNoise)
mkdir -p static
echo "Static files ready for deployment"
