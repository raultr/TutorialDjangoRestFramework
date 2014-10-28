from rest_framework import serializers # Para serializar el modelo
from authentication.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES #Para resaltar codigo en python


class SnippetSerializerConModelo(serializers.HyperlinkedModelSerializer):
   	#serializers.Field indica que el campo es de solo lectura
   	owner = serializers.Field(source='owner.username') 
   	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

	class Meta:
		model = Snippet
		fields = ('url', 'highlight', 'owner','title', 'code', 'linenos', 'language', 'style')
		

from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	#Trae los snippets relacionados con ese usuario
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail')
  	class Meta:
		model = User
		fields = ('url', 'username', 'snippets')
