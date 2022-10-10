# database-configurations
This repo stores all database configuration used for TraceIT

# Generating models.py using Django
1. Ensure Django settings has been configure to connect to the postgreSQL server.
2. To do so edit and replace the following database configuration with: (replace the <> respectively)
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database_name>',
        'USER': '<username>',
        'PASSWORD': '<password>',
        'HOST': '<IP address of the postgreSQL server>',
        'PORT': '5432',
    }
}
```
3. Using Django provided manage.py run the following command to generate the models.py and write it to a file.
```
python3 manage.py inspectdb > models.py
```

# How to import models.py into your app?
1. Go to the folder ```django_configurations``` and get the models.py files.
* mainsystem_models.py = contact tracer and building access database
* research_models.py = researcher database
2. Rename the file to models.py
3. Copy and paste the file into the app folder
4. Using manage.py and run the command ```python3 manage.py makemigrations <app name>```
5. This will create the migrations files used for the database
6. Using manage.py and run the command ```python3 manage.py migrate```
7. This will update your database and create the tables defined in the models.py

# Create users with limited permissions for local deployment
```bash
    export DJANGO_SECRET_KEY="test" \
        DJANGO_DEBUG="True" \
        VAULT_ADDR="http://127.0.0.1:8200" \
        VAULT_TOKEN="dev-only-token" \
        POSTGRES_HOST="127.0.0.1" \
        POSTGRES_PORT="5432" \
        POSTGRES_DB="test1" \
        POSTGRES_RESEARCH_DB="test2" \
        POSTGRES_AUTH_DB="test3" \
        POSTGRES_USER="test1" \
        POSTGRES_RESEARCH_USER="test2" \
        POSTGRES_AUTH_USER="test3" \
        POSTGRES_PASSWORD="test1" \
        POSTGRES_RESEARCH_PASSWORD="test2" \
        POSTGRES_AUTH_PASSWORD="test3" \
        POSTGRES_SUPER_USER="test4" \
        POSTGRES_SUPER_PASSWORD="test4"
```
1. Run `poetry run python roles_management/setup_db_roles.py` to generate 3 normal users for each database

# Setting up for PRODUCTION
## Installation and Setting environment variables
1. Ensure you have the following installed:
    * Python: `3.10` or above
2. Installing dependencies:
    1. Install poetry on your machine: https://python-poetry.org/
    2. Run `poetry install` to install the required dependencies.
3. Set and export the required environment variables:
    ```bash
    export DJANGO_SECRET_KEY="test" \
        DJANGO_DEBUG="True" \
        VAULT_ADDR="http://127.0.0.1:8200" \
        VAULT_TOKEN="dev-only-token" \
        POSTGRES_HOST="127.0.0.1" \
        POSTGRES_PORT="5432" \
        POSTGRES_DB="test1" \
        POSTGRES_RESEARCH_DB="test2" \
        POSTGRES_AUTH_DB="test3" \
        POSTGRES_USER="test1" \
        POSTGRES_RESEARCH_USER="test2" \
        POSTGRES_AUTH_USER="test3" \
        POSTGRES_PASSWORD="test1" \
        POSTGRES_RESEARCH_PASSWORD="test2" \
        POSTGRES_AUTH_PASSWORD="test3"
    ```
## Setup Phases

0. Ensure the respective databases are created and users configured.

1. Initialize all tables for each of the databases
For Research DB:
`poetry run python manage.py migrate researchs --database researchs_db`
For Main DB:
`poetry run python manage.py migrate main --database main_db`
For Auth DB:
`poetry run python manage.py migrate`

2. [optional] Generate mock data for main database 
Run `poetry run python sampledata/generate.py <number of users>` to generate <x> amount of users
Eg: `poetry run python sampledata/generate.py 1000`

3. Done


