from django.conf.urls import patterns, url

urlpatterns = patterns('request_response.views',
    url(r'^request_response/$', 'request_response_list'),
    url(r'^request_response/(?P<pk>[0-9]+)/$', 'request_response_detail'),
)


