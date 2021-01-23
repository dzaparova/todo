"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from main.views import homepage, test, second, third, index1, index2, index3
from django.conf import settings
from django.conf.urls.static import static
from bookstore.views import store 


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name= "home"),
    path("test/", test, name="test"),
    path("test2/", second),
    path("test3/", third),
    path("index1/", index1),
    path("index2/", index2),
    path("index3/", index3),
    path("store/", store)
]   +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)\
    +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

