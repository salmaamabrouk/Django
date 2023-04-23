from http.client import ResponseNotReady
from blog.models import Post, Comment
from urllib import response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from blog.serializers import BlogSerializer, Comment_Serializer
from rest_framework import generics

class Generic_Post_List(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Blog_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']

class Generic_Update_Post_List(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = Blog_Serializer


class Create_List_Retrieve_View_Set(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = Blog_Serializer


class Comment_List_Create_View(generics.ListCreateAPIView):
    serializer_class = Comment_Serializer

    def get_queryset(self):
        current_user_post = Post.objects.filter(owner = self.request.user)
        return Comment.objects.filter(owner = self.request.user)

 class Post_View_Set(viewsets.ModelViewSet):
     queryset = Post.objects.all()
     serializer = Blog_Serializer
     def list(self, request):
         queryset = Post.objects.all()
         serializer = Blog_Serializer
         return Response({'status': 'success', 'message': 'Posts retrieved successfully !', 'posts': serializer.data})

     def retrieve(self, request, *args, **kwargs):
         instance = self.get_object()
         serializer = self.get_serializer(instance)
         return Response({'status': 'success', 'message': 'Post retrieved successfully !', 'post': serializer.data})

     def create(self, request, *args, **kwargs):
         serializer = self.get_serializer(data = request.data)
         serializer.is_valid(raise_exception = True)
         self.perform_create(serializer)
         headers = self.get_success_headers(serializer.data)
         return Response({'status': 'success', 'message': 'Post created successfully !', 'post': serializer.data['id']}, status = status.HTTP_201_CREATED, headers = headers)

     def update(self, request, *args, **kwargs):
         partial = kwargs.pop('partial', False)
         instance = self.get_object()
         serializer = self.get_serializer(instance, data = request.data, partial = partial)
         serializer.is_valid(raise_exception = True)
         self.perform_update(serializer)
         return Response({'status': 'success', 'message': 'Post updated successfully !', 'post': serializer.data['id']})

     def destroy(self, request, *args, **kwargs):
         instance = self.get_object()
         self.perform_destroy(instance)
         return Response({'status': 'success', 'message': 'Post deleted successfully !'})