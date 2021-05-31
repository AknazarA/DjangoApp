"""mysite URL Configuration

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
from . import views
from django.conf.urls import include, url



urlpatterns = [
	#music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

	#music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #music/album/add/
    url(r'^album/add/$', views.CreateAlbum.as_view(), name='album-add'),

    #music/album/2/
    url(r'^album/(?P<pk>[0-9]+)/$', views.UpdateAlbum.as_view(), name='album-update'),

    #music/album/2/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.DeleteAlbum.as_view(), name='album-delete'),

]