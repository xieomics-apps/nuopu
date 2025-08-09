"""ag URL Configuration

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

from django.conf import settings
from django.conf.urls.static import static

#from google_site_verification import GOOGLE_SITE_VERIFICATION_URL


from django.urls import path, include

from django.contrib.sitemaps.views import sitemap
from basicapp.sitemaps import StaticViewSitemap
sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('basicapp.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
          name='django.contrib.sitemaps.views.sitemap'),
    #GOOGLE_SITE_VERIFICATION_URL,

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

