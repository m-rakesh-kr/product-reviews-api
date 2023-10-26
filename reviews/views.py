# class ProductViewSet(ReadOnlyModelViewSet):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#
#     """
#         path(irl) for extra method-> http://127.0.0.1:8000/product/1/extra_method/
#     """


# @action(detail=False)
# def get_list(self, request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)
#
# @action(detail=True)
# def get_product(self, request, pk=None):
#     product = Product.objects.get(pk=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)
#
# @action(detail=True, methods=['post', 'delete'])
# def delete_product(self, request, pk=None):
#     product = Product.objects.get(pk=pk)
#     product.delete()
#     return Response({'message': 'Product deleted successfully'})


from .serializers import ProductSerializer
from .models import Product
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_flex_fields.views import FlexFieldsMixin
from rest_flex_fields import is_expanded
from medium.authentication import CustomJWTAuthentication


class ProductViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]
    permit_list_expands = ['category', 'sites', 'comments', 'sites.company', 'sites.productsize']
    filterset_fields = ('category',)

    def get_queryset(self):
        queryset = Product.objects.all()

        if is_expanded(self.request, 'category'):
            queryset = queryset.prefetch_related('category')

        if is_expanded(self.request, 'comments'):
            queryset = queryset.prefetch_related('comments')

        if is_expanded(self.request, 'sites'):
            queryset = queryset.prefetch_related('sites')

        if is_expanded(self.request, 'company'):
            queryset = queryset.prefetch_related('sites__company')

        if is_expanded(self.request, 'productsize'):
            queryset = queryset.prefetch_related('sites__productsize')

        return queryset
