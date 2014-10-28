from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('snippets.urls')),  
    url(r'^', include('request_response.urls')),
    url(r'^', include('class_base_view.urls')),
    url(r'^', include('class_base_view_mixins.urls')),
    url(r'^', include('authentication.urls')),
)


urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)


