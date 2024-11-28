# Ecom
steps:
ctrl+shift+p 
create python virtual env
-------------------------
In terminal:
django-admin startproject name(in name type the the name for project)
cd name
python manage.py runserver(to run the server)
ctrl+c(to break the server)
python manage.py startapp name(In name name of the app)

-------------------------

In settings:
Add appname in the installed apps.
add templates in dirs.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Webapp',    
] 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

-----------------------------------------

create folders name:
templates(for html files)
static(for css,images)

-----------------------------------------
create files:
in app create files:
urls.py 
forms.py
-------------------------------------------
in project folder in urls:

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('appname.urls'))
]

in app urls:

from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="index"),
]
----------------------------------------
in views backend logic:
from django.shortcuts import render

def index(request):
    return render(request,"index.html")