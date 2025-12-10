# KaamConnect - Construction & Labour Platform

A Flask-based web application that connects customers, contractors, and labourers in the construction industry. The platform facilitates job postings, worker hiring, project management, and secure payments.

## Features

### For Customers
- Post construction projects and hire contractors
- Search and hire skilled labourers
- Track project progress and payments
- Rate and review contractors/labourers
- Manage multiple projects

### For Contractors
- Find construction projects
- Build and manage teams
- Hire skilled labourers
- Track project performance
- Access analytics and earnings

### For Labourers
- Find daily work opportunities
- Set availability and skills
- Receive payments on time
- Build reputation through ratings
- Track earnings

### For Admins
- Monitor platform activity
- Manage users (customers, contractors, labourers)
- View platform statistics
- Handle disputes and reports

## Project Structure

```
kaamconnect/
├── app.py                 # Main Flask application
├── utils.py              # Utility functions
├── requirements.txt      # Python dependencies
├── data/                 # JSON data storage
│   ├── admin.json       # Admin accounts
│   ├── contractors.json # Contractor accounts
│   ├── customers.json   # Customer accounts
│   └── labourers.json   # Labourer accounts
├── static/              # Static files
│   ├── css/            # Stylesheets
│   │   ├── main.css
│   │   ├── customer.css
│   │   ├── contractor.css
│   │   ├── labourer.css
│   │   ├── admin.css
│   │   └── dashboard.css
│   └── js/             # JavaScript files
│       ├── script.js
│       └── dashboard.js
└── templates/          # HTML templates
    ├── index.html
    ├── customer.html
    ├── customer_signin.html
    ├── contractor.html
    ├── contractor_signin.html
    ├── labourer.html
    ├── labourer_signin.html
    ├── admin.html
    └── dashboard/
        ├── base.html
        ├── customer_dashboard.html
        ├── contractor_dashboard.html
        ├── labourer_dashboard.html
        └── admin_dashboard.html
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Navigate to the project directory:**
   ```bash
   cd kaamconnect
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application:**
   ```bash
   python app.py
   ```

4. **Access the application:**
   - Open your browser and go to `http://localhost:5000`

## Usage

### First Time Setup

When you first run the application, it automatically creates the required data files in the `data/` directory.

### Default Admin Credentials

- **Username:** `admin`
- **Email:** `sagarmalideora@gmail.com`
- **Password:** `admin123`

⚠️ **Security Note:** Change these credentials in production!

### Creating Accounts

1. **Customer Registration:**
   - Click "Join as Customer" on the home page
   - Fill in full name, phone, email, and password
   - Account will be created and you can sign in

2. **Contractor Registration:**
   - Click "Join as Contractor" on the home page
   - Fill in company details and password
   - Account will be created and you can sign in

3. **Labourer Registration:**
   - Click "Join as Labourer" on the home page
   - Fill in name, phone, and password (email optional)
   - Account will be created and you can sign in

### User Workflows

**Customers:**
1. Sign up and create an account
2. Access customer dashboard
3. Post new projects or hire labourers
4. Manage active projects
5. Make payments
6. Write reviews

**Contractors:**
1. Sign up and create an account
2. Access contractor dashboard
3. Find available projects
4. Assemble and manage teams
5. Hire labourers
6. Track projects and earnings

**Labourers:**
1. Sign up and create an account
2. Access labourer dashboard
3. Find available jobs
4. Manage availability and skills
5. Track jobs and earnings

**Admins:**
1. Sign in with admin credentials
2. Access admin dashboard
3. View all users and statistics
4. Monitor platform activity

## API Endpoints

- `GET /api/stats` - Get platform statistics
- `GET /api/users` - Get all users (admin only)

## Authentication

The application uses:
- **Session-based authentication** for user login/logout
- **SHA-256 hashing** for password security
- **Role-based access control** with decorators

## Data Storage

Currently, the application uses **JSON files** for data storage in the `data/` directory:
- `admin.json` - Admin users
- `customers.json` - Customer accounts
- `contractors.json` - Contractor accounts
- `labourers.json` - Labourer accounts

⚠️ **Note:** For production, migrate to a proper database like PostgreSQL or MySQL.

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Icons:** Font Awesome 6.4.0
- **Storage:** JSON (development only)

## Security Considerations

1. **Change the secret key** in `app.py` for production
2. **Use HTTPS** in production
3. **Implement CSRF protection**
4. **Use a production WSGI server** (Gunicorn, uWSGI)
5. **Migrate to a proper database**
6. **Validate all user inputs**
7. **Rate limiting** for API endpoints
8. **CORS** configuration for API security

## Development

### Running in Debug Mode

The app runs in debug mode by default when executed with `python app.py`. This enables:
- Auto-reload on code changes
- Debugger enabled
- Detailed error pages

### Disabling Debug Mode

In `app.py`, change the last line:
```python
app.run(debug=False, port=5000)
```

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify the port in `app.py`:
```python
app.run(debug=True, port=8080)
```

### Template Not Found Error
Ensure the `templates/` directory exists with all required HTML files.

### Static Files Not Loading
Check that the `static/` directory exists with CSS and JS files properly organized.

### JSON Files Not Creating
Ensure the `data/` directory is writable and the application has permissions to create files.

## Future Enhancements

- [ ] Database migration (PostgreSQL/MySQL)
- [ ] Real-time messaging system
- [ ] Payment gateway integration
- [ ] GPS location tracking
- [ ] Mobile application
- [ ] Advanced analytics and reporting
- [ ] Machine learning for job recommendations
- [ ] Video verification system
- [ ] Dispute resolution system
- [ ] Referral program

## Support & Contact

**Developer:** Sagar Mali
- **Email:** sagarmalideora@gmail.com
- **Phone:** +91 9982760917
- **Location:** Pune, India

## License

This project is proprietary software. Unauthorized copying, modification, or distribution is prohibited.

## Disclaimer

This is a development version of KaamConnect. Use for testing and learning purposes only. For production deployment, follow all security best practices and legal requirements.

---

**Last Updated:** December 2025
