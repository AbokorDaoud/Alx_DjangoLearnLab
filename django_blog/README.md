# Django Blog Authentication System

This Django blog project implements a comprehensive user authentication system with the following features:

## Features
- User Registration
- User Login/Logout
- Profile Management
- Secure Password Handling
- CSRF Protection

## Authentication System Overview

### Registration
- Users can register using username, email, and password
- Custom registration form extends Django's UserCreationForm
- Email field is required
- Passwords are securely hashed

### Login/Logout
- Secure login using Django's authentication backend
- Remember me functionality
- Redirect to home page after login/logout
- Session management

### Profile Management
- Users can view and edit their profile
- Email updates supported
- Protected routes using @login_required decorator

## Testing the Authentication System

1. Registration Test:
   - Visit /register
   - Fill in username, email, and password
   - Submit form
   - Should redirect to profile page

2. Login Test:
   - Visit /login
   - Enter credentials
   - Submit form
   - Should redirect to home page

3. Profile Test:
   - Login required
   - Can view current details
   - Can update information
   - Changes should persist

4. Logout Test:
   - Click logout
   - Should redirect to home page
   - Protected routes should be inaccessible

## Security Features
- CSRF protection on all forms
- Secure password hashing
- Login required decorator for protected views
- Session security
- Form validation and sanitization
