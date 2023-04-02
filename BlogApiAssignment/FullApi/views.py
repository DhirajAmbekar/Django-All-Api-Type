from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Blog
from rest_framework.views import APIView
from .serializers import BlogsSerializer, RegisterSerializer
from django.contrib.auth.models import User


@api_view(["GET"])
def getRoutes(request):
        books = Blog.objects.all()
        serializer = BlogsSerializer(books, many=True)
        return Response(serializer.data)


class BlogAPI(APIView):
    def get(self, request):
        books = Blog.objects.filter(is_deleted=False)
        serializer = BlogsSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogsSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self , request):
        blog_id = request.data.get("id")
        BlogWork = Blog.objects.get(id=blog_id)
        serializer = BlogsSerializer(data=request.data, instance= BlogWork)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            blog_id = Blog.objects.get(id = id)
            BlogWork = Blog.objects.get(id=blog_id)
            serializer = BlogsSerializer(data=request.data, instance= BlogWork)
        return Response(serializer.data)
    
    def delete(self, request):
        Blog_id = request.data.get("id")
        BlogWork = Blog.objects.get(id=Blog_id)
        BlogWork.is_deleted = True
        BlogWork.save()
        return Response({"message": "Deleted"})


class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class GetUserAPI(APIView):
    def get(self, request):
        user = request.user.id
        data = User.objects.filter(id=user).values()
        return Response({"data": data})
