# Deployment Guide for Social Media API

## Prerequisites
- Python 3.8+
- PostgreSQL
- AWS Account (for S3 storage)
- Domain name (optional)

## Environment Variables
Create a `.env` file in production with the following variables:

```env
DEBUG=False
SECRET_KEY=your-secret-key
DJANGO_SETTINGS_MODULE=social_media_api.settings_prod

# Database
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432

# AWS S3
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name
AWS_S3_REGION_NAME=your_region

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

## Deployment Steps

### 1. Prepare the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate
```

### 2. Set Up PostgreSQL Database

1. Create a new PostgreSQL database
2. Update the database configuration in environment variables
3. Run migrations

### 3. Set Up AWS S3

1. Create an S3 bucket
2. Create an IAM user with S3 access
3. Configure bucket permissions
4. Update AWS credentials in environment variables

### 4. Deploy to Heroku

```bash
# Login to Heroku
heroku login

# Create a new Heroku app
heroku create your-app-name

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:hobby-dev

# Configure environment variables
heroku config:set DJANGO_SETTINGS_MODULE=social_media_api.settings_prod
heroku config:set SECRET_KEY=your-secret-key
# Add other environment variables...

# Deploy the application
git push heroku main

# Run migrations
heroku run python manage.py migrate
```

### 5. Set Up Custom Domain (Optional)

1. Add domain in Heroku settings
2. Configure DNS with your domain provider
3. Add SSL certificate

## Monitoring and Maintenance

### Logging
- Application logs: `heroku logs --tail`
- Check `logs/debug.log` for detailed error logs

### Database Backups
```bash
# Create backup
heroku pg:backups:capture

# Download backup
heroku pg:backups:download
```

### Updates and Maintenance
1. Regular dependency updates:
```bash
pip install -r requirements.txt --upgrade
```

2. Database maintenance:
```bash
python manage.py clearsessions
```

3. Monitor application health:
- Use Heroku metrics dashboard
- Set up error tracking (e.g., Sentry)

## Security Checklist

- [ ] Debug mode is disabled
- [ ] Secret key is properly set
- [ ] HTTPS is enforced
- [ ] Database credentials are secure
- [ ] AWS credentials are restricted
- [ ] CORS settings are configured
- [ ] Rate limiting is enabled
- [ ] File upload restrictions are in place

## Troubleshooting

### Common Issues

1. Static files not loading
   - Check STATIC_ROOT configuration
   - Run collectstatic
   - Verify whitenoise configuration

2. Database connection issues
   - Verify database credentials
   - Check database URL format
   - Ensure database is accessible

3. S3 storage issues
   - Verify AWS credentials
   - Check bucket permissions
   - Validate bucket region

## Support and Resources

- Django Documentation: https://docs.djangoproject.com/
- DRF Documentation: https://www.django-rest-framework.org/
- Heroku Django Guide: https://devcenter.heroku.com/articles/django-app-configuration
