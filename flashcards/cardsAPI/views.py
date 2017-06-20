
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
from cardsAPI.serializers import UserSerializer, DocumentSerializer, CardSerializer, DeckSerializer
from cardsAPI.models import *
from django.views.decorators.csrf import csrf_exempt


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

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class DeleteCardViewSet(views.APIView):
    def delete(self, request, format=None):
            req_body = json.loads(request.body.decode())
            print("\n\n{}".format(req_body['card']))

            data = "you did it"
            card_delete = Card.objects.get(pk=req_body['card'])

            try:
                card_delete.delete()
                return Response(data, content_type='application/json')
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    @csrf_exempt
    def patch(self, request, format=None):
            req_body = json.loads(request.body.decode())
            print("\n\n{}".format(req_body['card']))

            data = "you did it"
            card_edit = Card.objects.get(pk=req_body['card'])
            card_edit.front = req_body['card_front']
            card_edit.back = req_body['card_back']

            try:
                card_edit.patch()
                return Response(data, content_type='application/json')
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST) 


class GetCardsByDeckViewSet(views.APIView):
    def get(self, request, deck_id, format=None):

            # req_body= json.loads(request.body.decode())
            # print("\n\n{}".format(req_body['deck']))

            cards = Card.objects.filter(deck = deck_id)
            serializer = CardSerializer(cards, many=True)

            try:
                
                return Response(serializer.data, content_type='application/json')
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)  

class DeleteCardByIdViewSet(views.APIView):
    def delete(self, request, card_id, format=None):
            
           
            card = Card.objects.get(pk = card_id)
            card.delete()
            string = "mission accomplished"
            return Response(string)       



class CreateCardViewSet(views.APIView):
    def post(self, request, format=None):
            
            req_body = json.loads(request.body.decode())
            print("\n\n{}".format(req_body['deck']))
            

            deck_from_db = Deck.objects.get(pk=req_body['deck'])

            

            new_card = Card.objects.create(
                front = req_body['front'],
                back = req_body['back'],
                deck = deck_from_db
            )

            # token = Token.objects.get(user=request.user)
            data = json.dumps(request, indent=2)

            try:
                new_card.save()
                return Response(data)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)   

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

        







