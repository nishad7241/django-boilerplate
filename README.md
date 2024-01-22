# django-boilerplate

# Create virtual environment, activate it, and create a directory named src and enter to the directory.

    * virtualenv venv
    * source ../../venv/bin/activate
    * mkdir src
    * cd src

# install django and basic packages, create project and run the project.

    * pip install django
    * pip install pillow psycopg2-binary
    * pip install python-decouple
    * django-admin startproject  <project_name> (django-admin startproject django_boilerplate)
    * cd <project_name> (cd django_boilerplate)
    * mkdir static media templates
    * create settings.ini file
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
    * python manage.py runserver (default port 8000)
    * python manage.py runserver 0.0.0.0:<your_port> (Start the app - custom port)
    * python manage.py makemigrations && python manage.py migrate 
    * python manage.py createsuperuser (To Create super user)
    * To open python shell (To open python shell)
    * find . -path "*/migrations/*.py" -not -path "*/venv/*" -not -name "__init__.py" -delete && find . -path "*/migrations/*.pyc" -not -path "*/venv/*"  -delete (For Deleting Migrations)

# Update requirments.txt.

    * pip freeze > requirments.txt

#. Create custom apps based on the project requirments, Register on installed apps in settings.py.

    * python manage.py startapp <app_name> (python manage.py startapp core)
    * INSTALLED_APPS = [
        'core'
    ]

#. Configure Settings.py (ALLOWED_HOSTS, Templates, Database, Staic and Media roots)

    * ALLOWED_HOSTS = *, .localhost, .127.0.0.1,

    *   TEMPLATES = [
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

    *   DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql_psycopg2",
                "NAME": config("DB_NAME"),
                "USER": config("DB_USER"),
                "PASSWORD": config("DB_PASSWORD"),
                "HOST": config("DB_HOST"),
                "PORT": config("DB_PORT"),
            },
        }

    *   MEDIA_URL = '/media/'
        MEDIA_ROOT = BASE_DIR / 'media'
        STATIC_URL = '/static/'
        STATIC_FILE_ROOT = BASE_DIR / 'static'
        STATICFILES_DIRS = (BASE_DIR / 'static',)
        STATIC_ROOT = (BASE_DIR / 'static'/'static_files')

# Configure mail urls.py

    *   from django.contrib import admin
        from django.urls import include, path, re_path
        from django.conf import settings as SETTINGS
        from django.conf.urls.static import static


        urlpatterns = [
            path('realestate-admin/', admin.site.urls),

            path('core/', include(('core.urls', 'core'), namespace='core')),

        ] + static(SETTINGS.STATIC_URL, document_root=SETTINGS.STATIC_ROOT) + static(SETTINGS.MEDIA_URL, document_root=SETTINGS.MEDIA_ROOT)

# static_files directory, from where django-admin collectstatic will collect the static files.

    *   |---django_project
        |   |   | ...
        |   |   | ...
        |   |   |static_files (all static files we use in development)
        |   |   |---base (project as a whole specific static files)
        |   |   |   |---css
        |   |   |   |---img
        |   |   |   |---js
        |   |   |---core (my custom app specific)
        |   |   |   |---css
        |   |   |   |---img
        |   |   |   |---js
        |   |   | ...
        |   |   | ...

# templates directory as follows:

    *   |---django_project
        |   |   | ...
        |   |   | ...
        |   |---templates
        |   |   |---core (custom app specific)
        |   |   |---<other app specific templates>
        |   |   |---base.html (included basics of jquery and bootstrap)
        |   |   | ...
        |   |   | ...

# Overall folder structure used in this architecture is as follows:

    *   django_boilerplate
        |
        |---assets (folder created once static files are collected)
        |
        |---django_boilerplate
        |   |---apps
        |   |   |---core (custom app)
        |   |   |---...<other apps>...
        |   |   |---urls.py
        |   |
        |   |---config
        |   |   |---settings
        |   |   |   |---base.py
        |   |   |   |---settings.ini (ignored by git)
        |   |   |
        |   |   |---asgi.py
        |   |   |---urls.py
        |   |   |---wsgi.py
        |   |   |
        |   |   |static_files (all static files we use in development)
        |   |   |---base (project as a whole specific static files)
        |   |   |   |---css
        |   |   |   |---img
        |   |   |   |---js
        |   |   |---core (my custom app specific)
        |   |   |   |---css
        |   |   |   |---img
        |   |   |   |---js
        |   |   |
        |   |---templates
        |   |   |---core (custom app specific)
        |   |   |---<other app specific templates>
        |   |   |---base.py (included basics of jquery and bootstrap)
        |   |
        |   |---.gitignore
        |   |---manage.py
        |   |---requirements.txt
        |
        |---media (folder created once items were uploaded)
        |---db.sqlite3

# Database export and import

    * python manage.py dumpdata > database.json
    * python manage.py loaddata database.json
    * python manage.py dumpdata --exclude auth.permission --exclude contenttypes.contenttype --exclude sessions.session --exclude admin.logentry --indent 4 > data_base.json
