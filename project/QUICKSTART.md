# Project Setup Guide

## Install Nmap on your operating system 
This project uses the python3-nmap library, which is a Python wrapper around the nmap tool. While the python3-nmap package is included in the requirements.txt and installed via pip, the nmap binary must still be installed on the system to function correctly.
```bash
# Run
sudo apt-get update
sudo apt-get install nmap
```

## Troubleshooting Requirements Installation
```bash
# If encountering issues with requirements.txt installation
pip install --upgrade MarkupSafe certifi requests
```

## Virtual Environment Activation
```bash
# Navigate to project directory
cd project

# Activate virtual environment
source .venv/bin/activate
```

## Environment Variables Configuration

### Database Configuration (PostgreSQL)
```bash
# Database connection already exists in the settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vulnbyte',
        'USER': 'postgres',
        'PASSWORD': '@FINALPROJECT',
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}
```

## Create Database
If the PostgreSQL database doesn't already exist, you can quickly create it with the following Docker commands.
```bash
# First pull the PostgreSQL image
docker pull postgres

# Next run the container
docker run --name vulnbyte-db-fp -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=@FINALPROJECT -e POSTGRES_DB=vulnbyte -p 5432:5432 -d postgres

# To access PostgreSQL inside the container run
docker exec -it postgres-container psql -U postgres
```

## Running the Server
```bash
# Run the Django development server
# 'sudo' is used to run the command with superuser privileges, which might be needed for certain system-level tasks (e.g., using a privileged port).
# '$(which python3)' ensures that the correct Python 3 interpreter is used, even if multiple versions are installed.
sudo $(which python3) manage.py runserver
```

## Easy Navigation 
When registering an account pay attention to the terminal, there will be a link that activates your account and directs you to the login page.
```bash
# Register Page 
http://127.0.0.1:8000/authentication/register

# Login Page
http://127.0.0.1:8000/authentication/login
```

