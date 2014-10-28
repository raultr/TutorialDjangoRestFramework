from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from authentication import views


urlpatterns = patterns('authentication.views',
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
	url(r'^users/snippets/$',  views.SnippetListGeneric.as_view()),
    url(r'^users/snippets/(?P<pk>[0-9]+)/$', views.SnippetDetailGeneric.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)