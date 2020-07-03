from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .models import School
from .serializers import SchoolSerializer
from rest_framework.views import APIView
from rest_framework import status


class SchoolAPIView(APIView):

    def get(self, request):

        # school = Employee.objects.filter(role='Principal')
        school = School.objects.all()
        serializer = SchoolSerializer(school, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UpdateName(generics.UpdateAPIView):
#     queryset = ClientUser.objects.all()
#     serializer_class = ClientNameSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.name = request.data.get("name")
#         instance.save()
#
#         serializer = self.get_serializer(instance)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#
#         return Response(serializer.data)