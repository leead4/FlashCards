
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import views
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features
from rest_framework.parsers import FileUploadParser
# import json
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
        file_junk = request.FILES['file'].read()
        sting_file = file_junk.decode("utf-8") 
        
        # we need to translate our file into a string"



        sub = "Content-Type: text/plain"
        beg=0
        end=len(sting_file)
        print("im this long",len(sub))
        hey = sting_file.find(sub, beg, end)
        panda = hey + len(sub)
        pants = panda + 4
        print("this is it", pants)


        sub_2 = "------WebKitFormBoundary"
        beg_2 = 10
        
        hey_ya = sting_file.find(sub_2, beg_2)
        print("whooohoooooooooo", hey_ya)
       
        message = sting_file[pants:hey_ya]
        print("im tiny riiiiiiiick", message)


        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2017-02-27',
            username='3bb058ea-1ac0-417c-9180-de189bfa7232',
            password='qbGzw34uI4gI')

        response = natural_language_understanding.analyze(
            text= message,
            features=[features.SemanticRoles()])

        the_thing = json.dumps(response, indent=2)
        print(the_thing)




        return Response(the_thing, status=201)

        







