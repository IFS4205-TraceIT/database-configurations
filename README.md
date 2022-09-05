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

