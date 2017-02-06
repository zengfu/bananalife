"""bananalife URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ledctrl import views as mv
from . import views as root
import blog.views as blog
from django.conf import settings
from django.views.static import serve





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', root.index, name='index'),
    url(r'^handle_led',mv.handle_led,name='handle_led'),
    url(r'^test', mv.test, name='test'),
    url(r'^get_color', mv.get_color, name='get_color'),
    url(r'^blog/(\d*)', blog.blog, name='blog'),
    url(r'^page/(\d*)', blog.post, name='page'),
    url(r'^media/(?P<path>.*)$',serve,{'document_root': settings.MEDIA_ROOT})
]
