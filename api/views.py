from .models import Student
from .serializaers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from .customPermissions import MyPermission

class StudentModelViewSet(viewsets.ModelViewSet):
    # Basic Authentication:
    # queryset = Student.objects.all()
    # serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated,IsAdminUser]

    # IsAuthenticated will only check if user is logged in or not and allow to access url if user is logged in.
    # we can add common authentications like basic and IsAutheticated globally in settings.py folder.

    #  permission_classes = [AllowAny]
    # we can override global permission here by specifying permission to be applied for that class

    # Session Authentication:
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated,IsAdminUser]
    permission_classes = [MyPermission]

    # IsAuthenticatedReadOnly => it will allow autorised user to perform any request, Request for unauthorised
    # users will be permitted if the request method is one of the "safe" methods like "GET","HEAD" or "OPTIONS"

    # DjangoModelPermissions >> when used need to provide POST,change,update,delete permission in DB
    # DjangoModelPermissionsOrAnonReadOnly >> allows annonimus user to view data and need to provide permission in db for post,put,patch,delet