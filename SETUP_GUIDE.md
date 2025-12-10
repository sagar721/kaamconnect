# KaamConnect - Setup & Troubleshooting Guide

## ✓ What Has Been Fixed

### 1. **Project Structure**
- ✓ Verified all template files are present and correctly structured
- ✓ Verified all CSS and JavaScript files are in place
- ✓ Confirmed data directory exists with proper JSON file structure

### 2. **Python Environment**
- ✓ Created `requirements.txt` with Flask dependencies
- ✓ Created `config.py` for centralized configuration management
- ✓ Updated `app.py` to use configuration file instead of hardcoded values
- ✓ Verified Flask can be imported and runs successfully

### 3. **Documentation**
- ✓ Created comprehensive `README.md` with full documentation
- ✓ Created this troubleshooting guide
- ✓ Added code comments and docstrings throughout

### 4. **Convenience Scripts**
- ✓ Created `run.bat` for Windows users
- ✓ Created `run.sh` for Linux/Mac users
- ✓ Created `.gitignore` for version control

### 5. **Configuration**
- ✓ Centralized all configuration in `config.py`
- ✓ Set up secure password hashing with SHA-256
- ✓ Configured session management
- ✓ Added user role definitions

## 🚀 Quick Start

### Windows Users:
```bash
# Double-click run.bat or:
run.bat
```

### Linux/Mac Users:
```bash
# Make the script executable
chmod +x run.sh

# Run the script
./run.sh
```

### Manual Start:
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Access the Application:
- Open browser and go to: **http://localhost:5000**
- Admin login: `admin` / `admin123`

## 📋 File Inventory

### Core Application Files
- `app.py` - Main Flask application (590 lines)
- `utils.py` - Utility functions (109 lines)
- `config.py` - Configuration settings ✓ NEW
- `requirements.txt` - Python dependencies ✓ NEW
- `.gitignore` - Git ignore rules ✓ NEW

### Documentation
- `README.md` - Full project documentation ✓ NEW
- `SETUP_GUIDE.md` - This file ✓ NEW

### Startup Scripts
- `run.bat` - Windows startup script ✓ NEW
- `run.sh` - Linux/Mac startup script ✓ NEW

### Data Storage
- `data/admin.json` - Admin user (created on first run)
- `data/customers.json` - Customer accounts (created on first run)
- `data/contractors.json` - Contractor accounts (created on first run)
- `data/labourers.json` - Labourer accounts (created on first run)

### Templates (8 templates total)
- `templates/index.html` - Home page
- `templates/customer.html` - Customer signup
- `templates/customer_signin.html` - Customer login
- `templates/contractor.html` - Contractor signup
- `templates/contractor_signin.html` - Contractor login
- `templates/labourer.html` - Labourer signup
- `templates/labourer_signin.html` - Labourer login
- `templates/admin.html` - Admin login

### Dashboard Templates (5 templates total)
- `templates/dashboard/base.html` - Base template for all dashboards
- `templates/dashboard/customer_dashboard.html` - Customer dashboard
- `templates/dashboard/contractor_dashboard.html` - Contractor dashboard
- `templates/dashboard/labourer_dashboard.html` - Labourer dashboard
- `templates/dashboard/admin_dashboard.html` - Admin dashboard

### Static Assets
**CSS Files (6 files):**
- `static/css/main.css` - Main stylesheet
- `static/css/customer.css` - Customer page styles
- `static/css/contractor.css` - Contractor page styles
- `static/css/labourer.css` - Labourer page styles
- `static/css/admin.css` - Admin page styles
- `static/css/dashboard.css` - Dashboard styles

**JavaScript Files (2 files):**
- `static/js/script.js` - General scripts
- `static/js/dashboard.js` - Dashboard scripts

## ✅ Verification Checklist

- [x] Flask installed and imported successfully
- [x] All templates present and valid
- [x] All CSS files present and linked
- [x] All JavaScript files present and linked
- [x] Configuration file created and loaded
- [x] Data directory exists and has proper structure
- [x] App runs without errors
- [x] All routes accessible
- [x] Authentication system working
- [x] Session management configured

## 🔒 Security Notes

### Current Configuration (Development)
- Debug mode: ON
- Development server: Flask built-in
- HTTPS: Disabled
- CORS: Not configured

### For Production Deployment:

1. **Disable Debug Mode**
   ```python
   app.run(debug=False, port=5000)
   ```

2. **Change Secret Key**
   Edit `config.py`:
   ```python
   SECRET_KEY = 'your-super-secure-random-key-here'
   ```

3. **Use Production WSGI Server**
   ```bash
   pip install gunicorn
   gunicorn app:app --bind 0.0.0.0:5000
   ```

4. **Enable HTTPS**
   - Set up SSL/TLS certificate
   - Configure Flask to use HTTPS only

5. **Migrate to Real Database**
   - Replace JSON files with PostgreSQL/MySQL
   - Use SQLAlchemy ORM

6. **Add Rate Limiting**
   ```bash
   pip install Flask-Limiter
   ```

7. **Enable CORS if Needed**
   ```bash
   pip install flask-cors
   ```

8. **Change Default Credentials**
   - Update admin username/password in initialization

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Address already in use" on port 5000
**Solution:** Change port in `app.py` (last line):
```python
app.run(debug=True, port=8080)  # Use port 8080 instead
```

### Issue: "TemplateNotFound" error
**Solution:** Ensure you're running app from the correct directory:
```bash
cd /path/to/kaamconnect
python app.py
```

### Issue: Static files (CSS/JS) not loading
**Solution:** Check that:
1. `static/` directory exists
2. CSS files are in `static/css/`
3. JS files are in `static/js/`
4. Browser cache is cleared (Ctrl+Shift+Delete)

### Issue: Data not persisting (JSON files not created)
**Solution:**
1. Check if `data/` directory exists
2. Ensure application has write permissions
3. Run once with:
   ```bash
   python -c "from app import initialize_json_files; initialize_json_files()"
   ```

### Issue: Login not working
**Possible causes:**
- Check if JSON files in `data/` directory were created
- Verify password is at least 6 characters
- Check phone number is exactly 10 digits
- Check email format is valid

## 📱 Features Overview

### User Roles & Access

| Feature | Customer | Contractor | Labourer | Admin |
|---------|----------|-----------|----------|-------|
| Post Projects | ✓ | ✗ | ✗ | ✓ |
| Find Jobs | ✗ | ✓ | ✓ | ✓ |
| Manage Team | ✗ | ✓ | ✗ | ✗ |
| View Dashboard | ✓ | ✓ | ✓ | ✓ |
| Make Payments | ✓ | ✗ | ✗ | ✗ |
| Write Reviews | ✓ | ✓ | ✓ | ✗ |
| View Stats | ✓ | ✓ | ✓ | ✓ |
| Manage Users | ✗ | ✗ | ✗ | ✓ |

## 🎯 Next Steps

1. **Test All Features**
   - Create test accounts for each user type
   - Verify login/logout works
   - Check dashboards load correctly

2. **Review Security**
   - Change default admin password
   - Review session configuration
   - Plan database migration

3. **Add Enhancements**
   - Payment gateway integration
   - Email notifications
   - SMS alerts
   - Real-time messaging

4. **Deploy**
   - Set up production server
   - Configure domain/SSL
   - Monitor performance

## 📞 Support

If you encounter issues:

1. Check this guide's troubleshooting section
2. Review `README.md` for detailed documentation
3. Check Flask logs for error messages
4. Contact: sagarmalideora@gmail.com

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | Dec 2025 | Initial release with full project fixes |

---

**Status: ✓ Project Ready for Development**

All components have been verified and the application is ready to run!
