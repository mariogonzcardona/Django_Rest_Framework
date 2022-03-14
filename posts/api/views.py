# from django import http
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.permissions import IsAuthenticated,IsAdminUser
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly

# Para ModelViewSet:
class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True) # Para que solo se vean los publicados (published=True)
    # Metodos que pueden ser permitidos o no en una peticion:
    http_method_names = ['get','post','put','patch','delete']
    lookup_field = 'slug' # Para que el slug sea el identificador unico de cada post
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__slug'] # Para que solo se vean los posts de la categoria que se esta buscando
    
    
# Para ViewSet 
# class PostViewSet(ViewSet):
#     # Get all posts
#     def list(self,request):
#         posts=PostSerializer(Post.objects.all(),many=True)
#         return Response({"posts":posts.data},status=status.HTTP_200_OK)
#     # Get a post by id
#     def retrieve(self,request,pk:int):
#         post=Post.objects.get(pk=pk)
#         serializer=PostSerializer(post)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     # Create a post
#     def create(self,request):
#         serializer=PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)


# Para APIView 
# class PostApiView(APIView):
#     def get(self,request):
#         posts=PostSerializer(Post.objects.all(),many=True)
#         return Response({"posts":posts.data},status=status.HTTP_200_OK)
    
#     def post(self,request):
#         serializer=PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)