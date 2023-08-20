"""hello_django URL Configuration

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
from django.urls import re_path as url

from hello import views


urlpatterns = [
    url(r'^MyPublisher/', views.MyPublisher),
    url(r'^MyAuthor/', views.MyAuthor),
    url(r'^MyAuthorDetail/', views.MyAuthorDetail),
    url(r'^MyBook/', views.MyBook),
    url(r'^MyTermInfo/', views.MyTermInfo),
    url(r'^MyDevice/', views.MyDevice),
    url(r'^add_publisher/$', views.add_publisher, name='add_publisher'),
    url(r'^query_Publisher/$', views.query_Publisher, name='query_Publisher'),
    url(r'^query_Author/$', views.query_Author, name='query_Author'),
    url(r'^query_AuthorDetail/$', views.query_AuthorDetail, name='query_AuthorDetail'),
    url(r'^query_Book/$', views.query_Book, name='query_Book'),
    url(r'^query_TermInfo/$', views.query_TermInfo, name='query_TermInfo'),
    url(r'^query_Device/$', views.query_Device, name='query_Device'),
    url(r'^query_Device1/$', views.query_Device1, name='query_Device1'),
    url(r'^query_time/$', views.query_time, name='query_time'),
    url(r'^begin/$', views.begin, name='begin'),
]
