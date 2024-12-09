# Social Media API Project

## Description
This is my implementation of a Social Media API as part of the ALX Django Learning Lab. The project focuses on building a robust REST API using Django and Django REST Framework, with features like user authentication, profile management, and social interactions.

## Project Structure
The project is organized into the following components:
- `accounts`: Handles user authentication and profile management
- Custom User model with social features (follow/unfollow)
- Token-based authentication for secure API access

## Features Implemented
- User Registration and Authentication
- Custom User Profiles with:
  - Bio
  - Profile Picture
  - Follow/Unfollow functionality
- Token-based API Security

## Installation

1. Clone this repository:
```bash
git clone [your-repo-url]
cd social_media_api
```

2. Set up a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication Endpoints
- Register: `POST /api/accounts/register/`
- Login: `POST /api/accounts/login/`

### Profile Endpoints
- View/Update Profile: `GET/PUT /api/accounts/profile/`
- Follow User: `POST /api/accounts/follow/<user_id>/`
- Unfollow User: `POST /api/accounts/unfollow/<user_id>/`

## Usage Examples

### Register a New User
```bash
curl -X POST http://localhost:8000/api/accounts/register/ \
     -H "Content-Type: application/json" \
     -d '{
           "username": "testuser",
           "password": "securepassword",
           "password2": "securepassword",
           "email": "test@example.com",
           "first_name": "Test",
           "last_name": "User"
         }'
```

### Login
```bash
curl -X POST http://localhost:8000/api/accounts/login/ \
     -H "Content-Type: application/json" \
     -d '{
           "username": "testuser",
           "password": "securepassword"
         }'
```

## Authentication
To access protected endpoints, include your token in the request header:
```bash
Authorization: Token your-token-here
```

## Future Improvements
- Add post creation and management
- Implement comments and likes
- Add user search functionality
- Add direct messaging between users

## Author
[Your Name]
ALX Django Learning Lab Student
