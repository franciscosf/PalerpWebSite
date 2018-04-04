"""PalerpWebSite URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from apps.productos.views import tienda_view, prueba
from apps.general.views import clientes_view, index_view, nosotros_view, contactanos_view, productos_view, post_contactanos_view, usuario_view
from apps.user.views import signup_view, activate
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tienda/$', tienda_view, name = 'tienda'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^$', index_view, name = 'index'),
    url(r'^nosotros/$', nosotros_view, name = 'nosotros'),
    url(r'^usuario/$', login_required(usuario_view), name = 'usuario'),
    url(r'^signup/$', signup_view, name='signup'),
    url(r'^accounts/login/$', login, {'template_name':'views/login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name = 'logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),
    url(r'^productos/$', productos_view, name = 'productos'),
    url(r'^contactanos/$', contactanos_view, name = 'contactanos'),
    url(r'^clientes/$', clientes_view, name = 'clientes'),
    url(r'^test/', prueba, name = 'prueba'),
]
