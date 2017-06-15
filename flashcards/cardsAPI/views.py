
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from cardsAPI.serializers import UserSerializer, DocumentSerializer
from cardsAPI.models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer



class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, format=None):
        file_obj = request.data['file']
        print("here it is")
        return Response(status=204)

    def post(self, request, format=None):
        file_obj = (request.data['file'])

       
        print("whats up this is a file", file_obj)
        print("heres the type", type(file_obj))


        data = Document()

        data.description = 'bur'
        
        data.save()

        return Response(status=201)
        







