from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from class_base_view_mixins import views


urlpatterns = patterns('class_base_view_mixins.views',
    url(r'^class_base_view_mixins/$',  views.SnippetList.as_view()),
    url(r'^class_base_view_mixins/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^class_base_view_generics/$',  views.SnippetListGeneric.as_view()),
    url(r'^class_base_view_generics/(?P<pk>[0-9]+)/$', views.SnippetDetailGeneric.as_view()),
    url(r'^class_base_view_generics2/$',  views.SnippetListGeneric2.as_view()),
    url(r'^class_base_view_generics2/(?P<pk>[0-9]+)/$', views.SnippetDetailGeneric2.as_view()),

)

# Detalles sufijos: nos permiten pasar el tipo de formato que queremos
# http://localhost:8000/class_base_view_generics/.json
urlpatterns = format_suffix_patterns(urlpatterns)