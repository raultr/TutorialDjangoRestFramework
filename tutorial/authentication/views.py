from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from authentication.models import Snippet
from authentication.serializers import SnippetSerializerConModelo,UserSerializer
from django.contrib.auth.models import User
from authentication.permissions import IsOwnerOrReadOnly

class SnippetMixin(object):
    queryset = Snippet.objects.all()
    #paginate_by=1
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