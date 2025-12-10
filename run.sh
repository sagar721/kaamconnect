#!/bin/bash

# KaamConnect Startup Script for Linux/Mac

echo ""
echo "==================================="
echo "  KaamConnect - Startup Script"
echo "==================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

# Check if required files exist
if [ ! -f "app.py" ]; then
    echo "ERROR: app.py not found!"
    echo "Please run this script from the kaamconnect directory"
    exit 1
fi

if [ ! -f "requirements.txt" ]; then
    echo "ERROR: requirements.txt not found!"
    echo "Please ensure requirements.txt exists in the kaamconnect directory"
    exit 1
fi

# Create data directory if it doesn't exist
if [ ! -d "data" ]; then
    echo "Creating data directory..."
    mkdir -p data
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo ""
echo "Installing dependencies..."
python -m pip install --upgrade pip > /dev/null 2>&1
python -m pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

# Start the Flask application
echo ""
echo "==================================="
echo "Starting KaamConnect..."
echo "==================================="
echo ""
echo "The application will be available at: http://localhost:5000"
echo "Press CTRL+C to stop the server"
echo ""
echo "Default Admin Credentials:"
echo "  Username: admin"
echo "  Password: admin123"
echo ""
echo "==================================="
echo ""

python app.py

# Deactivate virtual environment on exit
deactivate
