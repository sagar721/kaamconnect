import json
import os
from datetime import datetime

def load_json_file(file_path):
    """Load JSON data from file"""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return []

def save_json_file(file_path, data):
    """Save data to JSON file"""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def format_currency(amount):
    """Format amount as Indian currency"""
    return f"₹{amount:,.2f}"

def format_date(date_string):
    """Format date string to readable format"""
    if isinstance(date_string, str):
        dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return dt.strftime("%d %b %Y, %I:%M %p")
    return ""

def calculate_progress(start_date, end_date):
    """Calculate project progress percentage"""
    start = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
    end = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
    now = datetime.now()
    
    total_duration = (end - start).days
    elapsed_duration = (now - start).days
    
    if total_duration <= 0:
        return 0
    if elapsed_duration >= total_duration:
        return 100
    
    return min(100, int((elapsed_duration / total_duration) * 100))

def generate_sample_projects(user_type, user_id):
    """Generate sample projects for demo"""
    projects = []
    
    if user_type == 'customer':
        projects = [
            {
                'id': 1,
                'title': 'Home Renovation',
                'contractor': 'BuildRight Constructions',
                'budget': 150000,
                'start_date': '2024-11-15T00:00:00',
                'end_date': '2024-12-30T00:00:00',
                'status': 'active',
                'progress': 65
            },
            {
                'id': 2,
                'title': 'Garden Landscaping',
                'contractor': 'Green Thumb Gardeners',
                'budget': 75000,
                'start_date': '2024-12-01T00:00:00',
                'end_date': '2024-12-30T00:00:00',
                'status': 'active',
                'progress': 30
            }
        ]
    elif user_type == 'contractor':
        projects = [
            {
                'id': 1,
                'title': 'Villa Construction',
                'customer': 'Mr. Sharma',
                'value': 4500000,
                'start_date': '2024-10-01T00:00:00',
                'end_date': '2025-03-31T00:00:00',
                'status': 'active',
                'progress': 40
            }
        ]
    
    return projects

def generate_sample_messages(user_type, user_id):
    """Generate sample messages for demo"""
    messages = []
    
    if user_type == 'customer':
        messages = [
            {
                'id': 1,
                'from': 'Rajesh Kumar (Contractor)',
                'message': "We'll start the painting work tomorrow at 9 AM...",
                'time': '2024-12-03T10:30:00',
                'unread': True
            },
            {
                'id': 2,
                'from': 'BuildRight Constructions',
                'message': 'Materials have been delivered to the site...',
                'time': '2024-12-02T14:15:00',
                'unread': False
            }
        ]
    
    return messages