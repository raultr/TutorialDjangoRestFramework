from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import detail_route
from hyperlinked.serializers import SnippetSerializerConModelo,UserSerializer
from authentication.models import Snippet
from rest_framework import permissions
from viewsets.permissions import IsOwnerOrReadOnly
from rest_framework import renderers
from rest_framework.response import Response

#Esta clase sustituye a las clases: UserList y UserDetail
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


#Esta clase sustituye a las clases: SnippetHighlight,SnippetListGeneric,SnippetDetailGeneric
class SnippetViewSet(viewsets.ModelViewSet):
	#This viewset automatically provides `list`, `create`, `retrieve`,
	#`update` and `destroy` actions.
	#Additionally we also provide an extra `highlight` action.
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializerConModelo
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def pre_save(self, obj):
		obj.owner = self.request.user