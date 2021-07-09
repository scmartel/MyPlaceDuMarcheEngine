
## URL CONFIGURATION 
## Adding new URL for the apps on seperate pages

"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path

#import views here
from reco_app.views import rec_create_view
from reco_app.views import userinput_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recommendation/', rec_create_view), ## add your view here
    path('', userinput_create_view)
]
