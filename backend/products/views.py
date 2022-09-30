from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # only called on CreateAPIView
    # used to add additional logic or create a django singal to do something before create
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title
        serializer.save(content=content)

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field = 'pk'


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# Mixins - Generic API view
class ProductMixinView(
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method 

    if method == 'GET':
        # detail view
        if pk is not None:
            # obj = Product.objects.filter(pk=pk)
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
       
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data 
        return Response(data)

    if method == 'POST':
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None

            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)


