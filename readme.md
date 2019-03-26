
**Core Packages**
from rest_framework.views import APIView
from rest_framework import mixins # Mix all  functions
from rest_framework import generics # generate APTVIEW

**URL Tips**
Run ......../snippets.api for API view
Run ......../snippets.json for json response
Run ......../pk for specific instance

**Learning Points**
Aim: Simplify process for usual request type (list, post, retrieve, put, delete)
1. view_one. Basic class type view. No longer need if statement to distinguish method type. 
2. view_two. Minis and generics class will have same performance by just accepting queryset and serializer_class. 
3. view_three. All functions are highly dense packaged for only two categories: ListCreateAPIView, RetrieveUpdateDestroyAPIView. 