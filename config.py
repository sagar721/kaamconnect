"""
Configuration settings for KaamConnect
"""

import os

# Flask Configuration
DEBUG = True
TESTING = False
SECRET_KEY = 'kaamconnect_secret_key_2025_secure_123'  # Change in production!

# Database
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# Session Configuration
PERMANENT_SESSION_LIFETIME = 86400  # 24 hours
SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# Upload Configuration
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

# User Roles
USER_ROLES = ['customer', 'contractor', 'labourer', 'admin']

# Validation Rules
MIN_PASSWORD_LENGTH = 6
PHONE_DIGITS = 10

# Email Configuration (optional)
MAIL_SERVER = None
MAIL_PORT = None
MAIL_USE_TLS = False
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_DEFAULT_SENDER = 'noreply@kaamconnect.com'

# Platform Settings
PLATFORM_NAME = 'KaamConnect'
PLATFORM_CURRENCY = '₹'
PLATFORM_COUNTRY = 'IN'

# Default admin user (created on first run)
DEFAULT_ADMIN = {
    'username': 'admin',
    'email': 'sagarmalideora@gmail.com',
    'password': 'admin123',
    'name': 'Admin User'
}
