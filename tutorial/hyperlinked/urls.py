from django.conf.urls import include,patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from hyperlinked import views

# API endpoints
urlpatterns = format_suffix_patterns(patterns('hyperlinked.views',
    url(r'^$', 'api_root'),
    url(r'^hyperlinked/snippets/$',
        views.SnippetListGeneric.as_view(),
        name='snippet-list'),
    url(r'^hyperlinked/snippets/(?P<pk>[0-9]+)/$',
        views.SnippetDetailGeneric.as_view(),
        name='snippet-detail'),
    url(r'^hyperlinked/snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url(r'^hyperlinked/users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^hyperlinked/users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
))

# Login and logout views for the browsable API
urlpatterns += patterns('',url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),)
