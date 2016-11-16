"""sta URL Configuration

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
from demo import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index,name='index'),
    url(r'^$', views.index),
    url(r'^about/$', views.about,name='about'),
    url(r'^acm/$', views.acm,name='acm'),
    url(r'^contact/$', views.contact,name='contact'),
    url(r'^hulianwang/$', views.hulianwang,name='hulianwang'),
    url(r'^lanqiao/$', views.lanqiao,name='lanqiao'),
    url(r'^portfolio/$', views.portfolio,name='portfolio'),
    url(r'^portfolio1/$', views.portfolio1,name='portfolio1'),
    url(r'^portfolio2/$', views.portfolio2,name='portfolio2'),
    url(r'^portfolio3/$', views.portfolio3,name='portfolio3'),
    url(r'^pricing/$', views.pricing,name='pricing'),
    url(r'^services/$', views.services,name='services'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
