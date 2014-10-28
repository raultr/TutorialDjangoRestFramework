from rest_framework import serializers # Para serializar el modelo
from authentication.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES #Para resaltar codigo en python


class SnippetSerializerConModelo(serializers.ModelSerializer):
   	#serializers.Field indica que el campo es de solo lectura
   	owner = serializers.Field(source='owner.username') 

	class Meta:
		model = Snippet
		fields = ('id', 'title', 'code', 'linenos', 'language', 'style','owner')


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	#Trae los snippets relacionados con ese usuario
    snippets = serializers.PrimaryKeyRelatedField(many=True)
   # titulo =  serializers.Field(source='snippets.title') 
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')