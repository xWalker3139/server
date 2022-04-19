"""my_project URL Configuration

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
from django.conf.urls import url, include
from my_app import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'my_app'

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'my_app/', include("my_app.urls", namespace='my_app')),
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^register/$', views.register_user, name="register_user"),
    url(r'^account/(?P<pk>\d+)/$', views.account, name="account"),
    url(r'logout_user', views.logout_user, name="logout_user"),
    url(r'^add_post/(?P<pk>\d+)/$', views.add_post, name="add_post"),
    url(r'^forum/$', views.forum, name="forum"),
    url(r'^search_forum/$', views.search_forum, name="search_forum"),
    url(r'^forum_details/(?P<pk>\d+)/$', views.forum_details, name="forum_details"),
    url(r'^update_post/(?P<pk>\d+)/$', views.update_post, name="update_post"),
    url(r'^delete_post/(?P<pk>\d+)/$', views.delete_post, name="delete_post"),
    url(r'^members/$', views.members, name="members"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
