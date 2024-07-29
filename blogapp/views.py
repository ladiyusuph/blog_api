from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListCreateView(APIView):
    def get(self, request):
        blogposts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogposts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostDetailUpdateView(RetrieveUpdateAPIView):
    serializer_class = BlogPostSerializer

    def get(self, request, pk):
        blogpost = BlogPost.objects.get(pk=pk)
        serializer = self.serializer_class(blogpost)
        return Response(serializer.data)

    def put(self, request, pk):
        blogpost = BlogPost.objects.get(pk=pk)
        serializer = self.serializer_class(blogpost, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostDeleteView(DestroyAPIView):
    def get(self, request, pk):
        blogpost = BlogPost.objects.get(pk=pk)
        blogpost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
