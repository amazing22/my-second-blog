from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'), # 추가
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}), # 추가
    url(r'', include('blog.urls')),
]
