from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('snippets.urls')),  
    url(r'^', include('request_response.urls')),
    url(r'^', include('class_base_view.urls')),
    url(r'^', include('class_base_view_mixins.urls')),
)




