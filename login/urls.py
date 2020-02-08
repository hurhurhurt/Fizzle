from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [url(r'^login/', include('login.urls')),
               url(r'^logout/', name='logout'),
               url(r'^admin/', admin.site.urls),
               ]
