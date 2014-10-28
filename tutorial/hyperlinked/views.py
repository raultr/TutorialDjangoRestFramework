from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from authentication.models import Snippet
from hyperlinked.serializers import SnippetSerializerConModelo,UserSerializer
from django.contrib.auth.models import User
from authentication.permissions import IsOwnerOrReadOnly


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

#Para poder hacer enlaces 
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class SnippetHighlight(generics.GenericAPIView):
	queryset = Snippet.objects.all()
	renderer_classes = (renderers.StaticHTMLRenderer,)

	def get(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)


class SnippetMixin(object):
    queryset = Snippet.objects.all()
    #paginate_by=2
    serializer_class = SnippetSerializerConModelo

class SnippetListGeneric(SnippetMixin, ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def pre_save(self, obj):
   		 obj.owner = self.request.user
   

class SnippetDetailGeneric(SnippetMixin, RetrieveUpdateDestroyAPIView):
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,) 

    def pre_save(self, obj):
        obj.owner = self.request.user

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer