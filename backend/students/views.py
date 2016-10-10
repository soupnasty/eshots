from django.db.models import Q

from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from classes.models import Class

from .models import Student
from .serializers import StudentSerializer, SearchSerializer


class ListCreateStudent(generics.ListCreateAPIView):
    """
    GET: Get a list of all the students
    POST: Create a new stduent
    """
    permission_classes = (AllowAny,)
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class GetUpdateStudent(generics.RetrieveUpdateAPIView):
    """
    GET: Get the details of a specific student
    PATCH: Update a specfici students info
    """
    permission_classes = (AllowAny,)
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentSearch(APIView):

    permission_classes = (AllowAny,)
    queryset = Student.objects.all()

    def post(self, request, *args, **kwargs):
        from django.conf import settings
        print(settings.FRONTEND_ROOT)
        data = SearchSerializer(data=request.data)
        data.is_valid(raise_exception=True)

        name_parts = data.validated_data['name'].split(' ')
        if len(name_parts) == 2:
            students = Student.objects.filter(first__icontains=name_parts[0]).filter(last__icontains=name_parts[1])
        else:
            students = Student.objects.filter(Q(first__icontains=name_parts[0]) | Q(last__icontains=name_parts[0]))

        result = StudentSerializer(students, many=True)
        return Response(result.data, status=status.HTTP_200_OK)
