
from django.http import Http404
from django.core.cache import cache

from .serializer import  BlogSerializer
from blog.models import Blog

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny



class BlogListView(APIView):
    """
    List all blogs in the case of a get request.
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

class BlogDetailView(APIView):
    """
    It retrieves a blog instance depending on the id.
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            blog = cache.get(f"blog_{pk}")
            if not blog:
                blog = Blog.objects.get(pk=pk)
                cache.set(f"blog_{pk}", blog, 600)

            return blog
        except Blog.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)



class BlogCreateView(APIView):
    """
     create a new one in the case of a post request.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            blog = Blog.objects.create(
                    title=request.data["title"], 
                    content=request.data["content"], 
                    author=request.user
                )
             
            cache.set(f"blog_{blog.id}", blog, 600)
            serializer = BlogSerializer(blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)


class BlogUpdateDeleteView(APIView):
    """
    It updates or deletes a blog instance depending on the id.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            blog = cache.get(f"blog_{pk}")

            if not blog:
                blog = Blog.objects.get(pk=pk)
                cache.set(f"blog_{pk}", blog, 600)

            return blog
        except Blog.DoesNotExist:
                raise Http404

    def put(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            if request.user == blog.author:
                updated_blog = serializer.save()

                if cache.get(f"blog_{pk}") is not None:
                    cache.delete(f"blog_{pk}")
                    cache.set(f"blog_{pk}", updated_blog, 600)
                    
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("Not authorized to edit", status=status.HTTP_403_FORBIDDEN)                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        if request.user == blog.author:
            blog.delete()
            if cache.get(f"blog_{pk}") is not None:
                cache.delete(f"blog_{pk}")
            return Response("Deleted successfully",status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("Not authorized to delete", status=status.HTTP_403_FORBIDDEN)   