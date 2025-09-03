#!/usr/bin/env python3

"""
Vercel build script for Django static files.
This script runs during Vercel deployment to collect static files.
"""

import os
import subprocess
import sys

def main():
    """Run Django's collectstatic during Vercel build."""
    print("Starting Vercel build process...")
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SpaceX.settings')
    
    try:
        # Import Django and configure
        import django
        from django.conf import settings
        from django.core.management import execute_from_command_line
        
        django.setup()
        
        print("Collecting static files...")
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--clear'])
        
        print("Static files collected successfully!")
        return 0
        
    except Exception as e:
        print(f"Build failed: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
