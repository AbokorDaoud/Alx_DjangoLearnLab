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

## Blog Post Features

### Post Management
The blog supports full CRUD (Create, Read, Update, Delete) operations for blog posts:

1. **View Posts**
   - Browse all posts at `/posts/`
   - View individual posts at `/post/<id>/`
   - Posts are paginated (5 posts per page)
   - Posts show author, publication date, and content preview

2. **Create Posts**
   - Authenticated users can create new posts at `/post/new/`
   - Required fields: title and content
   - Author is automatically set to current user

3. **Edit Posts**
   - Authors can edit their posts at `/post/<id>/edit/`
   - Only the post author can access edit functionality
   - Form pre-filled with existing content

4. **Delete Posts**
   - Authors can delete their posts at `/post/<id>/delete/`
   - Confirmation required before deletion
   - Only the post author can delete posts

### Security Features
- LoginRequiredMixin ensures only authenticated users can create posts
- UserPassesTestMixin verifies user ownership for edit/delete operations
- CSRF protection on all forms
- Secure routing and permission checks

### Testing Instructions
1. **Create Post Test**
   - Login to your account
   - Click "New Post" in navigation
   - Fill in title and content
   - Submit and verify post appears in list

2. **Edit Post Test**
   - View one of your posts
   - Click "Edit Post"
   - Modify content
   - Save and verify changes

3. **Delete Post Test**
   - View one of your posts
   - Click "Delete Post"
   - Confirm deletion
   - Verify post is removed

4. **Permission Test**
   - Try to edit/delete another user's post
   - Should be denied access
   - Verify only your posts show edit/delete options
