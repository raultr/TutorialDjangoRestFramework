from django.conf.urls import patterns, url
#from rest_framework.urlpatterns import format_suffix_patterns
from class_base_view import views


urlpatterns = patterns('class_base_view.views',
    url(r'^class_base_view/$',  views.SnippetList.as_view()),
    url(r'^class_base_view/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
)

