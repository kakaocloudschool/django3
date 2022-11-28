"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import board.views
import user.views
import app_deploy_history.views
import cluster.views


from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', user.views.login),
    path('member/', include('member.urls')),
    path('', auth_views.LoginView.as_view(template_name='member/login.html'), name='login'),
    
    path('board/list', board.views.list, name='board_list'),
    path('board/list/<int:bid>', board.views.list, name='board_list'),
    path('board/appcreate', board.views.appcreate, name='appcreate'),
    path('cluster/addcluster', cluster.views.addcluster, name='addcluster'),
    path('app_deploy_history/appdistribute', app_deploy_history.views.appdistribute, name='board_distribute'),
    path('board/appupdate', board.views.appupdate, name='board_update'),
    path('app_deploy_history/apphistory', app_deploy_history.views.apphistory, name='board_history'),
    path('board/appdelete/<int:bid>', board.views.appdelete, name='board_delete'),
    #path('board/read/<int:bid>', board.views.read),
    
    # path('user/signup', user.views.signup),
    # path('user/login', user.views.login, name='user_login'),
    path('user/logout', auth_views.LoginView.as_view(template_name='member/login.html'), name='login'),
    path('user/changepw', user.views.changepw, name='user_changepw'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""     path('board/create', board.views.create),
    
    
    path('board/update/<int:bid>', board.views.update), """