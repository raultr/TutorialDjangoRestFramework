from rest_framework import serializers # Para serializar el modelo
from request_response.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES #Para resaltar codigo en python


class SnippetSerializerConModelo(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')