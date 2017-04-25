"""insight01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from hello.engine import PcEngine,WxEngine
from helpers.director import urls as director_urls
from helpers.director import login_url
from employee import views as emp_views
from helpers.face import urls as face_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'pc/([\w\.]+)/?$',PcEngine.as_view(),name=PcEngine.url_name),
    url(r'wx/([\w\.]+)/?$',WxEngine.as_view(),name=WxEngine.url_name),
    url(r'^accounts/',include(login_url)),
    url(r'^my_info/?$',emp_views.my_info),
    url(r'^d/',include(director_urls)),
    url(r'^face/', include(face_urls)),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)