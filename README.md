# ContactApp

Python Django is used for creating this project.
Open the project in Pycharm or any other software,

Here "contact" is our projectname
and "contactapp" is our appname

==> RUN XXAMP and START APACHE, MYSQL
==> CREATE A DATABASE IN MYSQL NAMED "contactapp"

DATABASE CONFIGURATION (XXAMP..)
Database = Mysql (changed database configuration in "contacts/settings.py")(default database is mysqlite3)
=========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'contactapp',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
=========================
DatabaseName = contactapp
Table_Name = contacts

AFTER CREATING DATABASE IN MYSQL , open terminal
==>pip install mysql-client
==>python manage.py makemigrations
==>python manage.py migrate


Templates belongs to "Templates" Directory
[
homepage.html = HomePage 
signin.html = LoginPage
signup.html = Registration
]

CSS files belongs to "contactapp/static/css/<css_files>"

==>To run Project
>python manage.py runserver

