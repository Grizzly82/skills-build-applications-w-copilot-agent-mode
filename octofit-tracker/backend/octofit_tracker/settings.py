# Add 'rest_framework', 'djongo', 'corsheaders', and 'octofit_tracker' to the INSTALLED_APPS list
INSTALLED_APPS += [
    'rest_framework',
    'djongo',
    'corsheaders',
    'octofit_tracker',
]

# Add CORS middleware to the MIDDLEWARE list
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

# Configure the DATABASES setting to use MongoDB
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# Allow all hosts
ALLOWED_HOSTS = ['*']

# Enable CORS for all origins
CORS_ALLOW_ALL_ORIGINS = True