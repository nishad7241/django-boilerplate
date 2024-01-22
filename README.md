# django-boilerplate

1. Create virtual environment, activate it, and create a directory named src and enter to the directory.

    # virtualenv venv
    # source ../../venv/bin/activate
    # mkdir src
    # cd src

2. install django and basic packages, create project and run the project.

    # pip install django
    # pip install pillow psycopg2-binary
    # pip install python-decouple
    # django-admin startproject  <project_name> (django-admin startproject django_boilerplate)
    # cd <project_name> (cd django_boilerplate)
    # mkdir static media templates
    # create settings.ini file
    (
        [settings]

        DEBUG = True
        SERVER = False
        SQL = True
        ALLOWED_HOSTS= *, .localhost, .127.0.0.1,

        ; Postgresql details
        DB_NAME = django_boilerplate
        DB_USER = postgres
        DB_PASSWORD = postgres
        DB_HOST = localhost
        DB_PORT = 5432
    )
    # python manage.py runserver
    # python manage.py makemigrations && python manage.py migrate 
    # python manage.py createsuperuser (To Create super user)
    # To open python shell (To open python shell)
    # find . -path "*/migrations/*.py" -not -path "*/venv/*" -not -name "__init__.py" -delete && find . -path "*/migrations/*.pyc" -not -path "*/venv/*"  -delete (For Deleting Migrations)

3. Update requirments.txt.

    # pip freeze > requirments.txt

4. Create custom apps based on the project requirments, Register on installed apps in settings.py.

    # python manage.py startapp <app_name> (python manage.py startapp core)
    # INSTALLED_APPS = [
        'core'
    ]

5. Configure Settings.py (ALLOWED_HOSTS, Templates, Database, Staic and Media roots)

    # ALLOWED_HOSTS = *, .localhost, .127.0.0.1,

    #   TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [BASE_DIR / 'templates'],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]

    #   DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql_psycopg2",
                "NAME": config("DB_NAME"),
                "USER": config("DB_USER"),
                "PASSWORD": config("DB_PASSWORD"),
                "HOST": config("DB_HOST"),
                "PORT": config("DB_PORT"),
            },
        }

    #   MEDIA_URL = '/media/'
        MEDIA_ROOT = BASE_DIR / 'media'
        STATIC_URL = '/static/'
        STATIC_FILE_ROOT = BASE_DIR / 'static'
        STATICFILES_DIRS = (BASE_DIR / 'static',)
        STATIC_ROOT = (BASE_DIR / 'static'/'static_files')