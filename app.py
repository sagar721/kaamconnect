from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
import json
import os
from datetime import datetime
import hashlib
import re
from functools import wraps

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.secret_key = app.config['SECRET_KEY']

# Data directory
DATA_DIR = app.config['DATA_DIR']
os.makedirs(DATA_DIR, exist_ok=True)

# JSON file paths
CUSTOMERS_FILE = os.path.join(DATA_DIR, 'customers.json')
CONTRACTORS_FILE = os.path.join(DATA_DIR, 'contractors.json')
LABOURERS_FILE = os.path.join(DATA_DIR, 'labourers.json')
ADMIN_FILE = os.path.join(DATA_DIR, 'admin.json')

# Initialize JSON files if they don't exist
def initialize_json_files():
    files_data = {
        CUSTOMERS_FILE: [],
        CONTRACTORS_FILE: [],
        LABOURERS_FILE: [],
        ADMIN_FILE: [{
            'id': 1,
            'username': 'admin',
            'email': 'sagarmalideora@gmail.com',
            'password_hash': hashlib.sha256('admin123'.encode()).hexdigest(),
            'created_at': datetime.now().isoformat(),
            'name': 'Admin User',
            'role': 'super_admin'
        }]
    }
    
    for file_path, data in files_data.items():
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)

# Helper function to read JSON data
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Helper function to write JSON data
def write_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

# Helper function to validate email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Helper function to validate phone
def validate_phone(phone):
    return len(phone) == 10 and phone.isdigit()

# Generate unique ID
def generate_id(data_list):
    if not data_list:
        return 1
    ids = [item.get('id', 0) for item in data_list]
    return max(ids) + 1

# Authentication decorators
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session or 'user_type' not in session:
            flash('Please login first', 'error')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

def customer_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_type') != 'customer':
            flash('Access denied. Customer login required.', 'error')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

def contractor_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_type') != 'contractor':
            flash('Access denied. Contractor login required.', 'error')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

def labourer_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_type') != 'labourer':
            flash('Access denied. Labourer login required.', 'error')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_type') != 'admin':
            flash('Access denied. Admin login required.', 'error')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer')
def customer_page():
    return render_template('customer.html')

@app.route('/customer/signin')
def customer_signin_page():
    return render_template('customer_signin.html')

@app.route('/contractor')
def contractor_page():
    return render_template('contractor.html')

@app.route('/contractor/signin')
def contractor_signin_page():
    return render_template('contractor_signin.html')

@app.route('/labourer')
def labourer_page():
    return render_template('labourer.html')

@app.route('/labourer/signin')
def labourer_signin_page():
    return render_template('labourer_signin.html')

@app.route('/admin')
def admin_page():
    return render_template('admin.html')

# Authentication Routes
@app.route('/customer/signup', methods=['POST'])
def customer_signup():
    full_name = request.form.get('full_name', '').strip()
    phone = request.form.get('phone', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirm_password', '')
    
    # Validation
    if not all([full_name, phone, email, password, confirm_password]):
        flash('All fields are required!', 'error')
        return redirect(url_for('customer_page'))
    
    if password != confirm_password:
        flash('Passwords do not match!', 'error')
        return redirect(url_for('customer_page'))
    
    if len(password) < 6:
        flash('Password must be at least 6 characters long!', 'error')
        return redirect(url_for('customer_page'))
    
    if not validate_email(email):
        flash('Invalid email address!', 'error')
        return redirect(url_for('customer_page'))
    
    if not validate_phone(phone):
        flash('Invalid phone number! Must be 10 digits.', 'error')
        return redirect(url_for('customer_page'))
    
    # Read existing customers
    customers = read_json(CUSTOMERS_FILE)
    
    # Check if email or phone already exists
    for customer in customers:
        if customer['email'] == email:
            flash('Email already registered!', 'error')
            return redirect(url_for('customer_page'))
        if customer['phone'] == phone:
            flash('Phone number already registered!', 'error')
            return redirect(url_for('customer_page'))
    
    # Create new customer
    new_customer = {
        'id': generate_id(customers),
        'full_name': full_name,
        'phone': phone,
        'email': email,
        'password_hash': hashlib.sha256(password.encode()).hexdigest(),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat(),
        'status': 'active',
        'projects': [],
        'total_spent': 0,
        'active_projects': 0,
        'completed_projects': 0
    }
    
    customers.append(new_customer)
    write_json(CUSTOMERS_FILE, customers)
    
    flash('Account created successfully! Please sign in.', 'success')
    return redirect(url_for('customer_signin_page'))

@app.route('/customer/signin', methods=['POST'])
def customer_signin():
    identifier = request.form.get('identifier', '').strip()
    password = request.form.get('password', '')
    
    if not identifier or not password:
        flash('All fields are required!', 'error')
        return redirect(url_for('customer_signin_page'))
    
    customers = read_json(CUSTOMERS_FILE)
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Check if identifier is email or phone
    for customer in customers:
        if (customer['email'] == identifier or customer['phone'] == identifier) and customer['password_hash'] == password_hash:
            session['user_id'] = customer['id']
            session['user_type'] = 'customer'
            session['user_name'] = customer['full_name']
            session['user_email'] = customer['email']
            
            flash(f'Welcome back, {customer["full_name"]}!', 'success')
            return redirect(url_for('customer_dashboard'))
    
    flash('Invalid credentials! Please check your email/phone and password.', 'error')
    return redirect(url_for('customer_signin_page'))

@app.route('/contractor/signup', methods=['POST'])
def contractor_signup():
    company_name = request.form.get('company_name', '').strip()
    owner_name = request.form.get('owner_name', '').strip()
    phone = request.form.get('phone', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirm_password', '')
    
    # Validation
    if not all([company_name, owner_name, phone, email, password, confirm_password]):
        flash('All fields are required!', 'error')
        return redirect(url_for('contractor_page'))
    
    if password != confirm_password:
        flash('Passwords do not match!', 'error')
        return redirect(url_for('contractor_page'))
    
    if len(password) < 6:
        flash('Password must be at least 6 characters long!', 'error')
        return redirect(url_for('contractor_page'))
    
    if not validate_email(email):
        flash('Invalid email address!', 'error')
        return redirect(url_for('contractor_page'))
    
    if not validate_phone(phone):
        flash('Invalid phone number! Must be 10 digits.', 'error')
        return redirect(url_for('contractor_page'))
    
    # Read existing contractors
    contractors = read_json(CONTRACTORS_FILE)
    
    # Check if email or phone already exists
    for contractor in contractors:
        if contractor['email'] == email:
            flash('Email already registered!', 'error')
            return redirect(url_for('contractor_page'))
        if contractor['phone'] == phone:
            flash('Phone number already registered!', 'error')
            return redirect(url_for('contractor_page'))
    
    # Create new contractor
    new_contractor = {
        'id': generate_id(contractors),
        'company_name': company_name,
        'owner_name': owner_name,
        'phone': phone,
        'email': email,
        'password_hash': hashlib.sha256(password.encode()).hexdigest(),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat(),
        'status': 'active',
        'rating': 0,
        'completed_projects': 0,
        'active_projects': 0,
        'team_members': 0,
        'revenue': 0,
        'teams': []
    }
    
    contractors.append(new_contractor)
    write_json(CONTRACTORS_FILE, contractors)
    
    flash('Contractor account created successfully! Please sign in.', 'success')
    return redirect(url_for('contractor_signin_page'))

@app.route('/contractor/signin', methods=['POST'])
def contractor_signin():
    identifier = request.form.get('identifier', '').strip()
    password = request.form.get('password', '')
    
    if not identifier or not password:
        flash('All fields are required!', 'error')
        return redirect(url_for('contractor_signin_page'))
    
    contractors = read_json(CONTRACTORS_FILE)
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Check if identifier is email or phone
    for contractor in contractors:
        if (contractor['email'] == identifier or contractor['phone'] == identifier) and contractor['password_hash'] == password_hash:
            session['user_id'] = contractor['id']
            session['user_type'] = 'contractor'
            session['user_name'] = contractor['company_name']
            session['user_email'] = contractor['email']
            
            flash(f'Welcome back, {contractor["company_name"]}!', 'success')
            return redirect(url_for('contractor_dashboard'))
    
    flash('Invalid credentials! Please check your email/phone and password.', 'error')
    return redirect(url_for('contractor_signin_page'))

@app.route('/labourer/signup', methods=['POST'])
def labourer_signup():
    full_name = request.form.get('full_name', '').strip()
    phone = request.form.get('phone', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirm_password', '')
    
    # Validation
    if not all([full_name, phone, password, confirm_password]):
        flash('All fields except email are required!', 'error')
        return redirect(url_for('labourer_page'))
    
    if password != confirm_password:
        flash('Passwords do not match!', 'error')
        return redirect(url_for('labourer_page'))
    
    if len(password) < 6:
        flash('Password must be at least 6 characters long!', 'error')
        return redirect(url_for('labourer_page'))
    
    if email and not validate_email(email):
        flash('Invalid email address!', 'error')
        return redirect(url_for('labourer_page'))
    
    if not validate_phone(phone):
        flash('Invalid phone number! Must be 10 digits.', 'error')
        return redirect(url_for('labourer_page'))
    
    # Read existing labourers
    labourers = read_json(LABOURERS_FILE)
    
    # Check if phone already exists
    for labourer in labourers:
        if labourer['phone'] == phone:
            flash('Phone number already registered!', 'error')
            return redirect(url_for('labourer_page'))
        if email and labourer.get('email') == email:
            flash('Email already registered!', 'error')
            return redirect(url_for('labourer_page'))
    
    # Create new labourer
    new_labourer = {
        'id': generate_id(labourers),
        'full_name': full_name,
        'phone': phone,
        'email': email if email else '',
        'password_hash': hashlib.sha256(password.encode()).hexdigest(),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat(),
        'status': 'active',
        'rating': 0,
        'skills': ['General Labour'],
        'experience_years': 0,
        'completed_jobs': 0,
        'active_jobs': 0,
        'availability': True,
        'daily_wage': 800,
        'total_earnings': 0
    }
    
    labourers.append(new_labourer)
    write_json(LABOURERS_FILE, labourers)
    
    flash('Labourer account created successfully! Please sign in.', 'success')
    return redirect(url_for('labourer_signin_page'))

@app.route('/labourer/signin', methods=['POST'])
def labourer_signin():
    identifier = request.form.get('identifier', '').strip()
    password = request.form.get('password', '')
    
    if not identifier or not password:
        flash('All fields are required!', 'error')
        return redirect(url_for('labourer_signin_page'))
    
    labourers = read_json(LABOURERS_FILE)
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Check if identifier is email or phone
    for labourer in labourers:
        if (labourer['phone'] == identifier or (labourer['email'] and labourer['email'] == identifier)) and labourer['password_hash'] == password_hash:
            session['user_id'] = labourer['id']
            session['user_type'] = 'labourer'
            session['user_name'] = labourer['full_name']
            session['user_email'] = labourer['email'] if labourer['email'] else labourer['phone']
            
            flash(f'Welcome back, {labourer["full_name"]}!', 'success')
            return redirect(url_for('labourer_dashboard'))
    
    flash('Invalid credentials! Please check your phone/email and password.', 'error')
    return redirect(url_for('labourer_signin_page'))

@app.route('/admin/signin', methods=['POST'])
def admin_signin():
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '')
    
    if not username or not password:
        flash('All fields are required!', 'error')
        return redirect(url_for('admin_page'))
    
    admins = read_json(ADMIN_FILE)
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    for admin in admins:
        if (admin['username'] == username or admin['email'] == username) and admin['password_hash'] == password_hash:
            session['user_id'] = admin['id']
            session['user_type'] = 'admin'
            session['user_name'] = admin.get('name', 'Admin User')
            session['user_email'] = admin['email']
            
            flash('Admin login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
    
    flash('Invalid admin credentials!', 'error')
    return redirect(url_for('admin_page'))

# Dashboard Routes
@app.route('/dashboard/customer')
@login_required
@customer_required
def customer_dashboard():
    user_id = session.get('user_id')
    customers = read_json(CUSTOMERS_FILE)
    
    customer = next((c for c in customers if c['id'] == user_id), None)
    
    if not customer:
        flash('Customer not found', 'error')
        return redirect(url_for('customer_signin_page'))
    
    return render_template('dashboard/customer_dashboard.html', 
                         customer=customer,
                         stats=get_customer_stats(customer))

@app.route('/dashboard/contractor')
@login_required
@contractor_required
def contractor_dashboard():
    user_id = session.get('user_id')
    contractors = read_json(CONTRACTORS_FILE)
    
    contractor = next((c for c in contractors if c['id'] == user_id), None)
    
    if not contractor:
        flash('Contractor not found', 'error')
        return redirect(url_for('contractor_signin_page'))
    
    return render_template('dashboard/contractor_dashboard.html', 
                         contractor=contractor,
                         stats=get_contractor_stats(contractor))

@app.route('/dashboard/labourer')
@login_required
@labourer_required
def labourer_dashboard():
    user_id = session.get('user_id')
    labourers = read_json(LABOURERS_FILE)
    
    labourer = next((l for l in labourers if l['id'] == user_id), None)
    
    if not labourer:
        flash('Labourer not found', 'error')
        return redirect(url_for('labourer_signin_page'))
    
    return render_template('dashboard/labourer_dashboard.html', 
                         labourer=labourer,
                         stats=get_labourer_stats(labourer))

@app.route('/dashboard/admin')
@login_required
@admin_required
def admin_dashboard():
    user_id = session.get('user_id')
    admins = read_json(ADMIN_FILE)
    
    admin = next((a for a in admins if a['id'] == user_id), None)
    
    if not admin:
        flash('Admin not found', 'error')
        return redirect(url_for('admin_page'))
    
    return render_template('dashboard/admin_dashboard.html', 
                         admin=admin,
                         stats=get_admin_stats())

# Helper functions for dashboard stats
def get_customer_stats(customer):
    return {
        'active_projects': customer.get('active_projects', 0),
        'completed_projects': customer.get('completed_projects', 0),
        'total_spent': customer.get('total_spent', 0),
        'active_workers': 8  # Sample data
    }

def get_contractor_stats(contractor):
    return {
        'active_projects': contractor.get('active_projects', 0),
        'completed_projects': contractor.get('completed_projects', 0),
        'team_members': contractor.get('team_members', 0),
        'revenue': contractor.get('revenue', 0)
    }

def get_labourer_stats(labourer):
    return {
        'active_jobs': labourer.get('active_jobs', 0),
        'completed_jobs': labourer.get('completed_jobs', 0),
        'total_earnings': labourer.get('total_earnings', 0),
        'rating': labourer.get('rating', 0)
    }

def get_admin_stats():
    customers = read_json(CUSTOMERS_FILE)
    contractors = read_json(CONTRACTORS_FILE)
    labourers = read_json(LABOURERS_FILE)
    
    return {
        'total_customers': len(customers),
        'total_contractors': len(contractors),
        'total_labourers': len(labourers),
        'total_users': len(customers) + len(contractors) + len(labourers),
        'active_projects': 286,  # Sample data
        'platform_revenue': 1250000  # Sample data
    }

# Logout Route
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('index'))

# API endpoints
@app.route('/api/stats')
def get_stats():
    stats = get_admin_stats()
    return jsonify(stats)

@app.route('/api/users')
@login_required
@admin_required
def get_all_users():
    customers = read_json(CUSTOMERS_FILE)
    contractors = read_json(CONTRACTORS_FILE)
    labourers = read_json(LABOURERS_FILE)
    
    return jsonify({
        'customers': customers,
        'contractors': contractors,
        'labourers': labourers
    })

if __name__ == '__main__':
    initialize_json_files()
    app.run(debug=True, port=5000)