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
