"""django_server URL Configuration

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

import federatedsecure_app.federatedsecure_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('representations', federatedsecure_app.federatedsecure_app.path_representations),
    path('representation/<uuid:uuid>', federatedsecure_app.federatedsecure_app.path_representation_uuid),
    path('representation/<uuid:uuid>/<str:name>', federatedsecure_app.federatedsecure_app.path_representation_uuid_name),
]
