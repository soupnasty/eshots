from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Class
from .serializers import ClassSerializer


class ListCreateClass(generics.ListCreateAPIView):
    """
    GET: Get a list of all the students
    POST: Create a new stduent
    """
    permission_classes = (AllowAny,)
    serializer_class = ClassSerializer
    queryset = Class.objects.all()


class GetUpdateClass(generics.RetrieveUpdateAPIView):
    """
    GET: Get the details of a specific student
    PATCH: Update a specfici students info
    """
    permission_classes = (AllowAny,)
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
