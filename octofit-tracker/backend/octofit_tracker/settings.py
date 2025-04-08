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

# Add the codespace URL and localhost to ALLOWED_HOSTS
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'verbose-spork-rpwjvw6qv43pg5p-8000.app.github.dev']

# Enable CORS for all origins
CORS_ALLOW_ALL_ORIGINS = True