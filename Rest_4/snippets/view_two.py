from snippets.models import Snippet #
from snippets.serializers import SnippetSerializer #
from rest_framework import mixins # Mix all  functions
from rest_framework import generics # generate APTVIEW


class Snippetlist(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *var, **kvar):
        return self.list(request, *var, **kvar)

    def post(self, request, *var, **kvar ):
        return self.create(request, *var, **kvar)



class Snippetdetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *var, **kvar):
        return self.retrieve(request, *var, **kvar)
    def put(self, request, *var, **kvar):
        return self.update(request, *var, **kvar)
    def delete(self, request, *var, **kvar):
        return self.destroy(request, *var, **kvar)