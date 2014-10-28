from class_base_view.models import Snippet
from class_base_view.serializers import SnippetSerializerConModelo
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import generics

# ******** ClassBaseView Usando mixins ******************

#GenericAPIView Es una vista generica que provee filtros,paginacion etc.
#CreateModelMixin: Implementa la creacion del modelo y los mensajes de status 201 y 400
#ListModelMixin: Implementa el metodo .list para retornar una lista del modelo
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializerConModelo

    #Para obtener datos
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    #Para crear datos
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#GenericAPIView Es una vista generica que provee filtros,paginacion etc.
#RetrieveModelMixin Permite obtener datos del modelo existente
#UpdateModelMixin permite guardar y actualizar el modelo existente
#DestroyModelMixin permite eliminar el modelo existente
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializerConModelo

      #Para obtener datos
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

 	#Para crear datos
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    #Para eliminar datos
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ********* ClassBaseView Usando clases genericas ********************

#ListCreatAPIView hereda de: mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
#ListCreatAPIView procee get y post
#ListCreatAPIView representa una coleccion del modelo
class SnippetListGeneric(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializerConModelo


#RetrieveUpdateDestroyAPIView hereda de GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
#RetrieveUpdateDestroyAPIView provee get,put,patch,delete
#Representa un solo elemento del modelo
class SnippetDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializerConModelo


# ********* ClassBaseView Usando clases genericas y nuestro propio mixin********************


class SnippetMixin(object):
    queryset = Snippet.objects.all()
    paginate_by=1
    serializer_class = SnippetSerializerConModelo

class SnippetListGeneric2(SnippetMixin, ListCreateAPIView):
    pass

    # def get_paginate_by(self):
   	#  if self.request.accepted_renderer.format == 'json':
    #   	  return 1
   	#  return 100

class SnippetDetailGeneric2(SnippetMixin, RetrieveUpdateDestroyAPIView):
    pass